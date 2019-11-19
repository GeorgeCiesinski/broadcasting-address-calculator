# Broadcasting Address Calculator

The purpose of this script is to calculate a broadcasting address from an ip and subnet mask.

## Motivation

I created this script as a challenge to myself. I asked one of my colleagues who is also studying Python to share her assignments with me so that I can try my hand at the work she gets in school. Today I received her first assignment and threw this script together to meet the requirements.

## Usage

The script does not have any requirements and can be ran straight from Idle. It will prompt to enter:

ip, subnet

where subnet can either be a decimal ip value or CIDR. 

## Process

The script performs basic validation on the IP and the subnet mask / CIDR. After this, it builds the broadcasting address one octet at a time. This probably isn't the best way to do this, but I wanted to build this without outside help.
