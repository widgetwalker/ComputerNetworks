from ftplib import FTP

# Get user input
ftp_host = input("Enter FTP server address: ")
ftp_user = input("Enter FTP username: ")
ftp_pass = input("Enter FTP password: ")

try:
    # Connect and login
    ftp = FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_pass)
    print("✅ Connected to FTP server.")

    # List files in current directory
    print("\n📂 Files in current directory:")
    ftp.retrlines('LIST')

    # Ask if user wants to download a file
    download = input("\nDo you want to download a file? (yes/no): ").strip().lower()
    if download == 'yes':
        filename = input("Enter the filename to download: ")
        with open(filename, 'wb') as f:
            ftp.retrbinary(f'RETR {filename}', f.write)
        print(f"✅ File '{filename}' downloaded successfully.")

    ftp.quit()
    print("🔒 Connection closed.")

except Exception as e:
    print(f"❌ FTP error: {e}")
#ftp.py