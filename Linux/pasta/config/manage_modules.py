#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pasta.config.soft_import_module import soft_import
# browsers
from pasta.softwares.browsers.firefox_browsers import firefox_browsers
from pasta.softwares.browsers.chromium_browsers import chromium_browsers

# mails
from pasta.softwares.mails.thunderbird_mails import thunderbird_mails

try:
    from pasta.softwares.memory.memorydump import MemoryDump
except ImportError:
    pass


def get_categories():
    category = {
        'chats': {'help': 'Chat clients supported'},
        'sysadmin': {'help': 'SCP/SSH/FTP/FTPS clients supported'},
        'databases': {'help': 'SQL clients supported'},
        'mails': {'help': 'Email clients supported'},
        'memory': {'help': 'Retrieve passwords from memory'},
        'wifi': {'help': 'Wifi'},
        'browsers': {'help': 'Web browsers supported'},
        'wallet': {'help': 'Windows credentials (credential manager, etc.)'},
        'git': {'help': 'GIT clients supported'},
        'unused': {'help': 'This modules could not be used because of broken dependence'}
    }
    return category


def get_modules_names():
    return [
        ("pasta.softwares.mails.clawsmail", "ClawsMail"),
        ("pasta.softwares.databases.dbvis", "DbVisualizer"),
        ("pasta.softwares.sysadmin.env_variable", "Env_variable"),
        ("pasta.softwares.sysadmin.apachedirectorystudio", "ApacheDirectoryStudio"),
        ("pasta.softwares.sysadmin.filezilla", "Filezilla"),
        ("pasta.softwares.sysadmin.fstab", "Fstab"),
        ("pasta.softwares.browsers.opera", "Opera"),
        ("pasta.softwares.chats.pidgin", "Pidgin"),
        ("pasta.softwares.chats.psi", "PSI"),
        ("pasta.softwares.sysadmin.shadow", "Shadow"),
        ("pasta.softwares.sysadmin.aws", "Aws"),
        ("pasta.softwares.sysadmin.docker", "Docker"),
        ("pasta.softwares.sysadmin.rclone", "Rclone"),
        ("pasta.softwares.sysadmin.ssh", "Ssh"),
        ("pasta.softwares.sysadmin.cli", "Cli"),
        ("pasta.softwares.sysadmin.gftp", "gFTP"),
        ("pasta.softwares.sysadmin.keepassconfig", "KeePassConfig"),
        ("pasta.softwares.sysadmin.grub", "Grub"),
        ("pasta.softwares.databases.sqldeveloper", "SQLDeveloper"),
        ("pasta.softwares.databases.squirrel", "Squirrel"),
        ("pasta.softwares.wifi.wifi", "Wifi"),
        ("pasta.softwares.wifi.wpa_supplicant", "Wpa_supplicant"),
        ("pasta.softwares.wallet.kde", "Kde"),
        ("pasta.softwares.wallet.libsecret", "Libsecret"),
        ("pasta.softwares.memory.mimipy", "Mimipy"),
        ("pasta.softwares.git.gitforlinux", "GitForLinux")
    ]

    # very long to execute
    # try:
    # 	module_names.append(MemoryDump())
    # except:
    # 	pass


def get_modules():
    modules = [soft_import(package_name, module_name)() for package_name, module_name in get_modules_names()]
    return modules + chromium_browsers + firefox_browsers + thunderbird_mails
