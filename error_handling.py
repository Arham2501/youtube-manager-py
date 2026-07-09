# Error Handling and File Handling

file = open('youtube.txt','w')
# Both Try-finally and with syntax are same, use anyone one
try:
    file.write('chai aur code')
finally:
    file.close()


with open('youtube.txt','w') as file:
    file.write('chai aur python')
