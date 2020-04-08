resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC58o4bTeIivrumnISGUlpz4Orn2eUDtJYIKdI/3MaNS9A5QLC+CJZ/g/hcMcYvs5OsrgNWeQFmXxgx5wpjBIzb/H9RaJRXsdoS6gp/X57yyeQvBzPXH9udyK7l26pE8rlQDlN7zTHjSVFDmlXGQWvjYGo0ZxFxtca1AYWnBzst/OEBxXPmH6Nb7zdeh829EcNVLhho5jWwBsc1hFPU4vM9NKRoE4nWuK/55KFleyPzf/SmK+bO2qMHrM6ggTy8MkHvWcv952jJJ7ufS6fH43Nues9Eb2rUUsRAwt5/hiUy5jGupz7fO9FzgULeDY5LXpDjN8PJgOWWgakTxIGhgN8r sumeshks29@gmail.com"
}

variable "region" {
  default = "eu-west-1"
}
variable "AmiLinux" {
  type = "map"
  default = {
    eu-west-1 = "ami-9398d3e0" # Ireland
  }
  description = "I add only 3 regions (Virginia, Oregon, Ireland) to show the map feature but you can add all the regions that you need"
}

variable "aws_access_key" {
  default = "AKIATUS3MVVJPULFL47T"
  description = "the user aws access key"
}

variable "aws_secret_key" {
  default = "/zp4d6RNuj0fYHCOwJ0O9euusSe5vr3pYWGbtqtV"
  description = "the user aws secret key"
}

variable "credentialsfile" {
  default = "/home/sura/.aws/credentials" #replace your home directory
  description = "where your access and secret_key are stored, you create the file when you run the aws config"
}

variable "vpc-fullcidr" {
    default = "172.28.0.0/16"
  description = "the vpc cdir"
}
variable "Subnet-Public-AzA-CIDR" {
  default = "172.28.0.0/24"
  description = "the cidr of the subnet"
}
variable "Subnet-Private-AzA-CIDR" {
  default = "172.28.3.0/24"
  description = "the cidr of the subnet"
}
variable "key_name" {
  default = "deployer-key"

  description = "the ssh key to use in the EC2 machines"
}
variable "DnsZoneName" {
  default = "tvarit-dev.com"
  description = "the internal dns name"
}


