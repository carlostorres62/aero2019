String alt;
String dep1;
String dep2;
String dep3;
String weight;
String Data;
int count = 0;
int count2 = 1;
int count3 = 0;
String data = (String)count2;



void setup(){
  Serial.begin (9600);
  
}

void loop(){
while(true){
    
  alt = count++; 
  weight = count++;
  if (count < 10){
    dep1 = count3;
  }
  else{
    dep1 = count++;
  }
  if (count < 30){
    dep2 = count3;
  }
  else{
    dep2 = count++;
  }
  if (count < 500){
    dep3 = count3;
  }
  else{
    dep3 = count++;
  }

    
    data = count2++;
    Data = data + "," + alt + "," + dep1 + "," + dep2 + "," + dep3 + "," + weight;
    Serial.println(Data);
    delay(1000);    
  }
}
