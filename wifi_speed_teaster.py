import speedtest as spdt

st = spdt.Speedtest()

# print('Download: ', st.download())
# print('Upload: ', st.upload())

st.get_servers([])

# print('Ping: ', st.results.ping)

run = True
while run == True:
    
    print('Download: ', st.download())
    print('Upload: ', st.upload())

    print('Ping: ', st.results.ping)

    a = input()
    if a == "q" or a == "q ":
        run = False