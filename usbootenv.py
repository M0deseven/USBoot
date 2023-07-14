import os
import subprocess
main_menu = '''\
####################################
##### quit - exits the program #####
##### fusb - format usb        #####
##### wrusb - write iso to usb #####
##### lsblk - list filesystems #####
####################################
'''
def dev_umount():
    print('unmounting drive')
    if '0' not in str(os.system(f'sudo -S umount /dev/{selected_drive}')):
            if f'├─{selected_drive}{range(10)}' or f'└─{selected_drive}{range(10)}' in subprocess.getoutput(['lsblk']):
                for i in range(10):
                    os.system(f'sudo -S umount /dev/{selected_drive}{i} > /dev/null')
    print('drive unmounted')


def dev_format():
    print('format selected drive? [y/n]')
    confirmation = input('CONFIRMATION>>')
    if confirmation.lower() == 'y':
        print('formating...')
        os.system(f'sudo -S mkfs.vfat -I /dev/{selected_drive}')
        print('format complete')


def dev_write():
    print('Writing iso to drive')
    os.system(f'sudo -S dd if={isopath} of=/dev/{write_dev} status=progress')
    print('### BOOTABLE USB IS READY ###')
    input('[Back]')


while True:
    print('\n')
    print('### USBOOT v0.2 ###')
    print('select a mode')
    print(main_menu)
    mode  = input('MAIN//MENU> ')
    if mode == 'quit':
        print('exiting.')
        break
    if mode == 'fusb':
        os.system('lsblk')
        print('Enter a drive name to format')
        print('Ex: "sda", "sdb"')
        selected_drive = input('DRIVE//SELECT>> ')
        while True:
            #invalid_exceptions = [f'{str(range(10))},', '/']
            if f' {selected_drive} ' in subprocess.getoutput('lsblk'):
                if selected_drive not in str(range(10)):
                    print('drive found')
                    break
            if selected_drive.lower() == 'back':
                print('returning.')
                break
            else:
                print('Drive not found, enter a valid drive name.')
                print('enter "back" to return')
                selected_drive =  input('>> ')
        print('format selected drive? [y/n]')
        confirmation = input('CONFIRMATION>>')
        if confirmation.lower() == 'y':
            dev_umount()
            dev_format()
        if confirmation.lower() == 'n':
            print('Format Aborted. Returning to main menu')
        else:
            print('Invalid input. Returning to main menu')
    if mode == 'lsblk':
        print('###FILESYSTEMS AND MOUNTPOINTS###')
        os.system('lsblk')
        input('[Back]')
    if mode == 'wrusb':
        print('Enter path to .iso')
        isopath = input('> ')
        os.system('lsblk')
        print('Enter device to write to')
        print('Ex: "sda", "sdb"')
        write_dev = input('> ')
        print(f'Confirm writing {isopath} to {write_dev} [y/n]')
        write_confirm = input('> ')
        if write_confirm.lower() == 'y':
            dev_write()
        if write_confirm.lower() == 'n':
            print('Aborting.') 

