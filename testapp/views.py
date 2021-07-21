from django.shortcuts import render
import json
from cmath import exp,pi
# Create your views here.
def recursive_fft(a):
	n=len(a)
	if n==1:
		return a
	wn=exp(2*pi*complex(1j)/n)
	w=1
	b=a[::2]
	c=a[1::2]
	y=recursive_fft(b)
	z=recursive_fft(c)
	d=[0 for i in range(len(a))]
	for k in range(0,n//2):
		d[k]=y[k]+w*z[k]
		d[k+n//2]=y[k]-w*z[k]
		w=w*wn
		print("KUNAL")
	return d
def inverse_fft(a):
	n=len(a)
	if n==1:
		return a
	wn=exp(2*pi*complex(-1j)/n)
	w=1
	b=a[::2]
	c=a[1::2]
	y=recursive_fft(b)
	z=recursive_fft(c)
	d=[0 for i in range(len(a))]
	for k in range(0,n//2):
		d[k]=(y[k]+w*z[k])/n
		d[k+n//2]=(y[k]-w*z[k])/n
		w=w*wn
		print("KUNAL")
	return d
def home(requests):
	arr1=requests.GET.get('input')
	b=arr1.split(',')
	a=[int(i) for i in b]
	arr2=recursive_fft(a)
	return render(requests,'testapp/index.html',{'array1':arr2,'array2':arr1})
def home1(requests):
	arr1=requests.GET.get('input1')
	b=arr1.split(',')
	a=[complex(i) for i in b]
	arr2=inverse_fft(a)
	return render(requests,'testapp/index.html',{'array3':arr1,'array4':arr2})
def index(requests):
	return render(requests,'testapp/index.html')