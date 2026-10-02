# V-Server Setup
Create a test Virtual Server for learning purposes
(loom intro link https://www.loom.com/share/3f5aaa8fc3f2492cb031a0f775497776)

Guide: [PDF Checklist](https://github.com/MajoNeko/VServer/blob/main/Docs/Git_VServer_Checkliste.pdf)

In this walkthrough you will learn how to setup SSH keys on a virtual server, disable password authentication in favour of using SSH authentication, installing and configuring a web server and setting up a Git account with username, email and SSH key on your server.



## Setup and copy SSH keys

### Step 1 - Generate an SSH key pair 
In the terminal type the following: 
```bash
ssh-keygen -t ed25519 -f C:/Users/user-directory/.ssh/id_ed25519_VServer -C "key name comment"
```
> [!Note]
> -t ed25519 : This will generate a new SSH key pair using Ed25519 key type (recommended as it is faster, shorter and has better security properties).

> -f ~/.ssh/id_ed25519_VServer : Specifies where the key pair should be generated (filename, usefull for organization purposes and for multiple key pairs)

> -C "key name comment" : provides a comment for the key pair

### Step 2 : Verify your SSH key pairs 
You can view your key pairs using the foloowing command:
```bash
    ls ~/.ssh
```
> [!Note]
> ~ represents your home directory

### Step 3 - Test your server connection
Connect to the server using the following command:
 ```bash
    ssh user@ip-address   
```

If you are able to connect to the server then you can log off and move on to the next step.
```bash
    logout
```

### Step 4 - Copying your SSH key
Copy your SSH public key to the authorized_key file using the following command:
```bash
    ssh-copy-id -i C:/Users/user-directory/.ssh/id_ed25519_VServer.pub user@ip-address
```
> [!Note]
> -i stands for identity

### Step 6 - Test your connection using the SSH key:
```bash
    ssh -i C:/Users/user-directory/.ssh/id_ed25519_VServer user@ip-address
```
