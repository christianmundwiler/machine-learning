import mosspy

userid = 305917884

m = mosspy.Moss(userid, "python")

m.addBaseFile("/Users/christianmundwiler/Documents/school/fall22/csci4930/hw/PA3/PA3-4930-clustering.ipynb")

# Submission Files
m.addFile("/Users/christianmundwiler/Documents/school/fall22/csci4930/hw/PA3/PA3-4930-clustering-Mundwiler.ipynb")
m.addFilesByWildcard("/Users/christianmundwiler/Documents/school/fall22/csci4930/hw/sophie/Assignment-04/Sondericker_Assignment04.ipynb")

# progress function optional, run on every file uploaded
# result is submission URL
url = m.send(lambda file_path, display_name: print('*', end='', flush=True))
print()

print ("Report Url: " + url)

# Save report file
m.saveWebPage(url, "submission/report.html")

# Download whole report locally including code diff links
mosspy.download_report(url, "submission/report/", connections=8, log_level=10, on_read=lambda url: print('*', end='', flush=True)) 
# log_level=logging.DEBUG (20 to disable)
# on_read function run for every downloaded file
