import os
from opencc import OpenCC
import sqlite3
from alive_progress import alive_bar
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import shutil


def main():
    messagebox.showinfo('步驟一', '請選取YGOpro cards.cdb 檔案位址')
    sqlite_filename = askopenfilename(title="請選取YGOpro cards.cdb 檔案位址", filetypes=[("Data base", "*.cdb")])
    sqlite_backup_filename = sqlite_filename.replace("cards.cdb", "cards_backup.cdb")
    conn = sqlite3.connect(sqlite_filename)
    if os.path.exists(sqlite_backup_filename):
        print(sqlite_backup_filename)
        os.remove(sqlite_backup_filename)
    shutil.copyfile(sqlite_filename, sqlite_backup_filename)
    c = conn.cursor()
    c2 = conn.cursor()
    print("資料庫簡轉繁")
    cursor = c.execute("SELECT id, name, desc, str1, str2, str3, str4, str5 from texts")
    total = len(cursor.fetchall())
    cursor = c.execute("SELECT id, name, desc, str1, str2, str3, str4, str5 from texts")
    with alive_bar(total, force_tty=True) as bar:
        for row in cursor:
            if row[0] == 1174075:
                c2.execute("UPDATE texts set name = \'{}\' where ID={}"
                           .format("龍輝巧-扶筐增二μβ\'\'", row[0]))
            else:
                c2.execute("UPDATE texts set name = \'{}\' where ID={}"
                           .format(cc.convert(row[1]).replace('\'', '\\\''), row[0]))
            c2.execute("UPDATE texts set desc = \'{}\' where ID={}"
                       .format(cc.convert(row[2]).replace('\'', '\\\''), row[0]))
            c2.execute("UPDATE texts set str1 = \'{}\' where ID={}"
                       .format(cc.convert(row[3]).replace('\'', '\\\''), row[0]))
            c2.execute("UPDATE texts set str2 = \'{}\' where ID={}"
                       .format(cc.convert(row[4]).replace('\'', '\\\''), row[0]))
            c2.execute("UPDATE texts set str3 = \'{}\' where ID={}"
                       .format(cc.convert(row[5]).replace('\'', '\\\''), row[0]))
            c2.execute("UPDATE texts set str4 = \'{}\' where ID={}"
                       .format(cc.convert(row[6]).replace('\'', '\\\''), row[0]))
            c2.execute("UPDATE texts set str5 = \'{}\' where ID={}"
                       .format(cc.convert(row[7]).replace('\'', '\\\''), row[0]))
            bar()  # 進度條
        conn.commit()
    print("資料庫簡轉繁成功")
    conn.close()
    messagebox.showinfo('步驟二', '請選取YGOpro strings.conf 檔案位址')
    conf_filename = askopenfilename(title="請選取YGOpro strings.conf 檔案位址", filetypes=[("設定檔", "*.conf")])
    conf_backup_filename = conf_filename.replace("strings.conf", "strings_backup.conf")
    if os.path.exists(conf_backup_filename):
        os.remove(conf_backup_filename)
    shutil.copyfile(conf_filename, conf_backup_filename)
    print("系統文件簡轉繁")
    fo = open(conf_filename, "r")
    fo2 = open(conf_filename, "r+")
    filedata = fo2.read()
    lines = fo.readlines()
    with alive_bar(len(lines), force_tty=True) as bar:
        for line in lines:
            if line.split(' ')[0] == "!system":
                filedata = filedata.replace(line.split(' ')[2].split('\n')[0]
                                            , cc.convert(line.split(' ')[2].split('\n')[0]))
            elif line.split(' ')[0] == "!counter":
                filedata = filedata.replace(line.split(' ')[2].split('\n')[0]
                                            , cc.convert(line.split(' ')[2].split('\n')[0]))
            elif line.split(' ')[0] == "!setname":
                filedata = filedata.replace(line.split(' ')[2].split('\t')[0].split('\n')[0]
                                            , cc.convert(line.split(' ')[2].split('\t')[0].split('\n')[0]))
            else:
                pass
            bar()  # 進度條
    fo.close()
    fo2.seek(0)
    fo2.write(filedata)
    fo2.close()
    print("系統文件簡轉繁成功")


if __name__ == '__main__':
    cc = OpenCC('s2tw')
    root = tk.Tk()
    root.withdraw()
    main()
