float[] values;
int j=0;
void setup() {
  size(1200, 800);
  //fullScreen();
  values=new float[width];

  for ( int i=0; i<values.length; ++i ) {
    values[i]=random(height);
  }
}

void draw() {
  background(0);
  for ( int i=0; i<1000; ++i ) {
    if (j<values.length-1)
      if (values[j] > values[j+1])
        swap(values, j, j+1);

    j++;
    if (j==values.length)
      j=0;
  }



  for ( int i=0; i<values.length; ++i ) {
    stroke(255);
    line(i, height, i, height-values[i]);
  }
}

void swap(float[] arr, int a, int b) {
  float temp=arr[a];
  arr[a]=arr[b];
  arr[b]=temp;
}
