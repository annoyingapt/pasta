from pasta.config.soft_import_module import soft_import

mozilla_module_location = "pasta.softwares.browsers.mozilla", "Mozilla"
Mozilla = soft_import(*mozilla_module_location)

# Name, path
thunderbird_mails = [
    (u'thunderbird', u'.thunderbird'),
]

thunderbird_mails = [Mozilla(browser_name=name, path=path, category='mails') for name, path in thunderbird_mails]
