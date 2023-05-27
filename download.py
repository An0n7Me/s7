from polyglot.downloader import downloader

downloader.download("LANG:fr")

print(downloader.is_installed("LANG:fr"))