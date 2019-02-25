path = "C:/Users/Administrator/Desktop/python_learing/a/b/c/test.txt.txt"
parts = path.rsplit('/', 1)
dirname = parts[0]
filename = parts[1]

parts = filename.split('.')
ext = parts[1]

#ext_idx = filename.find('.')


print("dir: ", dirname)
print("file:", filename)
print("ext: ", ext)



                          

                          

