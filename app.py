from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.pipeline.diabetes_predict_pipeline import Customdata
from src.pipeline.diabetes_predict_pipeline import Predictpipeline
from src.pipeline.cad_predict_pipeline import Cad_customdata
from src.pipeline.cad_predict_pipeline import Cad_predictpipeline
from langchain_groq import ChatGroq

print("All the files got imported")
application=Flask(__name__)
app=application

@app.route('/')
def index():
   return render_template('home.html')

@app.route("/diabetes_predict",methods=["POST","GET"])
def prediction():
   if request.method=="GET":
      return render_template('diabetes.html')
   else:
      data=Customdata(
         Gender=request.form.get('Gender'),
         AGE=request.form.get('AGE'),
         Urea=request.form.get('Urea'),
         Cr=request.form.get('CR'),
         Chol=request.form.get('Chol'),
         TG=request.form.get('TG'),
         HDL=request.form.get('HDL'),
         LDL=request.form.get('LDL'),
         VLDL=request.form.get('VLDL'),
         BMI=request.form.get('BMI')

      )
     

      pred_data=data.covert_data_into_df()

      predict_data=Predictpipeline()
      result,result_prob=predict_data.predict(pred_data)

      result_lst=result_prob[0]

      def largest_element(lst):
         largest=lst[0]
         place=0
         for i in range(0,3):
            if lst[i]>largest:
                  largest=lst[i]
                  place+=i

         return largest   
      
      largest=largest_element(result_lst)

      def place(lst,element):
         names={
             0:"non-diabetic",
             1:"diabetic",
             2:"prediabetic"

         }
         for i in range(len(lst)):
            if lst[i]==element:
                  return names[i]
      
      gender = request.form.get('Gender')
      age = request.form.get('AGE')
      urea = request.form.get('Urea')
      cr = request.form.get('Cr')
      chol = request.form.get('Chol')
      tg = request.form.get('TG')
      hdl = request.form.get('HDL')
      ldl = request.form.get('LDL')
      vldl = request.form.get('VLDL')
      bmi = request.form.get('BMI')
            
            

      rag_query = (
         f"My gender is {gender}, age is {age}. "
         f"Urea is {urea}, creatinine is {cr}. "
         f"Cholesterol is {chol}, triglycerides are {tg}, HDL is {hdl}, LDL is {ldl}, VLDL is {vldl}. "
         f"BMI is {bmi}. Explain these terms simply in detail and provide practical steps to control or reduce diabetes risk."
      )

      llm=ChatGroq(groq_api_key="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",model_name="gemma2-9b-it",temperature=0.1,max_tokens=1024)

      prompt=f"""Use the following context to answer the question concisely.
            
            Question: {rag_query}

            Answer:"""

      response_text=llm.invoke(prompt)


      return render_template('diabetes.html',response=response_text,val1=largest_element(result_lst)*100,val2=place(result_lst,largest))

@app.route('/predict_cad',methods=['GET','POST'])
def pred():
   if request.method=="GET":
      return render_template('cad.html')
   else:
      data=Cad_customdata(
         age=request.form.get('age'),
         sex=request.form.get('sex'),
         chest_pain_type=request.form.get('chest_pain_type'),
         resting_bp_s=request.form.get('resting_bp_s'),
         cholesterol=request.form.get('cholesterol'),
         fasting_blood_sugar=request.form.get('fasting_blood_sugar'),
         resting_ecg=request.form.get('resting_ecg'),
         max_heart_rate=request.form.get('max_heart_rate'),
         exercise_angina=request.form.get('exercise_angina'),
         oldpeak=request.form.get('oldpeak'),
         ST_slope=request.form.get('ST_slope')

      )
      pred_data=data.covert_data_into_df()

      predict_data=Cad_predictpipeline()
      result,result_prob=predict_data.predict(pred_data)

      result_pro=result_prob[0]
      name={
          0:"absence of disease",
          1:"Presence of this dieases"
      }



      def largest(lst):
         large=0
         index=0
         first_element=lst[0]
         second_element=lst[1]

         if first_element>second_element:
                  large=first_element
                  index=0
         else:
                  large=second_element
                  index=1
         return large ,index        

      r,index=largest(result_pro)
      result=round(r, 2)
      ind=name[index]       
      
      age=request.form.get('age'),
      sex=request.form.get('sex'),
      chest_pain_type=request.form.get('chest_pain_type'),
      resting_bp_s=request.form.get('resting_bp_s'),
      cholesterol=request.form.get('cholesterol'),
      fasting_blood_sugar=request.form.get('fasting_blood_sugar'),
      resting_ecg=request.form.get('resting_ecg'),
      max_heart_rate=request.form.get('max_heart_rate'),
      exercise_angina=request.form.get('exercise_angina'),
      oldpeak=request.form.get('oldpeak'),
      ST_slope=request.form.get('ST_slope')

      cad_query = (
         f"My age is {age}, sex is {sex}. "
         f"My chest pain type is {chest_pain_type}. "
         f"My resting systolic BP is {resting_bp_s} mmHg. "
         f"My cholesterol is {cholesterol} mg/dL, fasting blood sugar flag is {fasting_blood_sugar}, "
         f"resting ECG is {resting_ecg}, max heart rate is {max_heart_rate} bpm, exercise-induced angina is {exercise_angina}. "
         f"Oldpeak is {oldpeak} and ST slope is {ST_slope}. "
         f"Explain these terms simply in detail and tell practical steps to reduce CAD risk."
      )
      llm=ChatGroq(groq_api_key="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",model_name="gemma2-9b-it",temperature=0.1,max_tokens=1024)

      prompt=f"""Use the following context to answer the question concisely.
               
               Question: {cad_query}

               Answer:"""

      response_text=llm.invoke(prompt)              
    
 

      return render_template('cad.html',result=result*100,index=ind,response=response_text)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)   