import paramiko
import base64
import io
import signal
# config
# host = '192.168.0.139'
# username = 'ubuntu'
# password = 'ubuntu'
# cmd = 'sudo service postgresql stop'


host = '192.168.0.77'
username = 'ubuntu'
password = 'ubuntu'
# cmd = 'sudo service odoo-server restart'
# host = 'xxx.xxx.xxx.xxx'
# username = 'ubuntu'
# password = ''
# cmd = 'sudo /etc/init.d/odoo-server restart'
# cmd = 'tail -f /var/log/odoo/odoo-prod.log'
cmd = 'sudo service postgresql status | echo 1'
# cmd = 'sudo ps ax | grep odoo'
# key_path = '/home/ubnutu/Documents/remote_pem_file.pem'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# key = paramiko.RSAKey.from_private_key_file(key_path)
# client.connect(host, username=username, password=password, pkey=key)
client.connect(host, username=username, password=password)

# stdin, stdout, stderr = client.exec_command('sudo ps ax | grep odoo')
# stdin, stdout, stderr = client.exec_command('sudo ps ax | grep odoo',get_pty=True)
stdin, stdout, stderr = client.exec_command(cmd, get_pty=True)
stdin.write(password + '\n')
# stdout.read()

for line in stdout:
    print(line.strip('\n'))

client.close()


#k = paramiko.RSAKey.from_private_key_file("/Users/whatever/Downloads/mykey.pem")
#c.connect( hostname = "www.acme.com", username = "ubuntu", pkey = k )
# from PIL import Image
# pdf_1 = base64.b64decode(orders.partner_id.image)
#
# img = Image.open(io.BytesIO(pdf_1))
# img.save('imagetoadd.bmp')
# worksheet.write(2, 2, ' ', base_style)
# # line_cnt = 2
# # worksheet.write_merge(line_cnt, line_cnt, 1, 2, '', base_style)
# worksheet.insert_bitmap('imagetoadd.bmp', 2, 1, scale_x=.11, scale_y=.08)
