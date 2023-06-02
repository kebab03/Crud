from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import requests
import json
# import cv2

class KivyApp(App):
	firebase_url= "https://cloudproget-default-rtdb.europe-west1.firebasedatabase.app/.json"
	
	def build(self):
		box_layout = BoxLayout()
		box_layout.orientation ='vertical'

		button = Button (text = " Patch data")

		button_get = Button (text = "Get Data")
		button_get.bind(on_press=self.creat_get)
		
		self.inp_x=TextInput(text="input _X: ")
		box_layout.add_widget(self.inp_x)
		


		self.inp_y = TextInput(text='input _Y: ',multiline=False)
		box_layout.add_widget(self.inp_y)



		button_post = Button (text = " post data")
		button_post.bind(on_press=self.creat_post)

		button_put = Button (text = " put data ")
		button_put.bind(on_press=self.creat_put)

		button_delete = Button (text = " delete data")
		button_delete.bind(on_press=self.creat_delete)
		
		self.mylabel=Label(text="Favorite Color: ")
		box_layout.add_widget(self.mylabel)
		

		button.bind(on_press=self.creat_patch)
		

		box_layout.add_widget(button)
		box_layout.add_widget(button_get)
		box_layout.add_widget(button_post)
		box_layout.add_widget(button_put)
		box_layout.add_widget(button_delete)
	

		return box_layout

	def creat_patch(self,*args):
		
		#self.mylabel.text = "Uploaded!"
		print('button patch clicked')
		json_data='{"umrl":"yahcgoogle.com","codp":"2mmmmrwef"}'
		res = requests.patch(url=self.firebase_url,json=json.loads(json_data))
		print('res::',res)

	def creat_get(self,*args):
		#self.mylabel.text = "Uploaded!"
		print('button GET clicked')
		res = requests.get(url=self.firebase_url)
		print('res_json::',res.json())
	
	def creat_post(self,*args):
		print("self.inp_x::",self.inp_x.text)
		print("self.inp_Y::",self.inp_y.text)
		 
		print('button POST clicked')
		json_data= {"x":self.inp_x.text,"y":self.inp_y.text}
		#jjson_data1=str({"x":'77',"y":'9'})
		json_data1='{"x":"76","y":"8"}'
		#json_data1=str({"x":self.inp_x.text,"y":self.inp_y.text})
		#json_data2="'"+json_data1+"'"
		#json_data3='"'+json_data+'"'
		data_in_json=json.dumps(json_data)
		# print("json_data:::,type(json_data)",json_data,type(json_data))
		# print("json_data1:::,type(json_data1)",json_data1,type(json_data1))
		# print("json_data2:::,type(json_data2)",json_data2,type(json_data2))
		# print("json_data3:::,type(json_data3)",json_data3,type(json_data3))
		res=requests.post(url=self.firebase_url,json=json.loads(data_in_json))
		print('res::',res.json())

	def creat_put (self,*args):
		
		#self.mylabel.text = "Uploaded!"
		print('button put clicked')
		json_data='{"Table":{"umrl":"hgcccgoogle.com","codp":"2mmmmrwef"}}'
		res=requests.put(url=self.firebase_url,json=json.loads(json_data))
		print('res::',res)
	
	def creat_delete(self,*args):
		delete_url= "https://cloudproget-default-rtdb.europe-west1.firebasedatabase.app/"

		#self.mylabel.text = "Uploaded!"
		print('button delete clicked')
		#json_data='{"umrl":"hgcccgoogle.com","codp":"2mmmmrwef"}'
		res=requests.delete(url= delete_url+"Table/umrl"+".json")
		print('res::',res)
	

 
if __name__ == '__main__':
	KivyApp().run()		

