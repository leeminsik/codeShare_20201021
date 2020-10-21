#!/usr/bin/env python
# coding: utf-8

# code description
# Author : minsik.lee
# FileName : testCode_201021.py
# Note 
    # @Summary : IRP - Input Data
    # @version 1.0 : (2020-10-21) draft


from dotenv import load_dotenv
import os

if __name__ == "__main__":
	load_dotenv()
	print(os.getenv("S3_ACCESS_KEY"))

