package com.aniketdhuri.lba.lba;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {
    final Context context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {


                open_camera();





            }
        });
    }
    static final int REQUEST_CAMERA = 1;
    public  void open_camera(){

        Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(intent, REQUEST_CAMERA);

    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);



        if(requestCode==1) {

            new MyAsyn(this).execute(true);

        }
        if (requestCode==2)
        {
            // Bitmap thumbnail = (Bitmap) data.getExtras().get("data");
            // ByteArrayOutputStream bytes = new ByteArrayOutputStream();
            //thumbnail.compress(Bitmap.CompressFormat.PNG, 100, bytes);
            // File destination = new File(Environment.getExternalStorageDirectory(),"temp.jpg");

            Bitmap thumbnail = (Bitmap) data.getExtras().get("data");
            ByteArrayOutputStream bytes = new ByteArrayOutputStream();
            thumbnail.compress(Bitmap.CompressFormat.PNG, 100, bytes);

            java.io.File destination = new java.io.File((MainActivity.this
                    .getApplicationContext().getFileStreamPath("temp.png")
                    .getPath()));

            FileOutputStream fo;
            try {
                fo = new FileOutputStream(destination);
                fo.write(bytes.toByteArray());
                fo.close();
            } catch (IOException e) {
                e.printStackTrace();
            }

           // new uploadFileToServerTask().execute(destination.getAbsolutePath());
        }
    }



}

 class MyAsyn extends AsyncTask<Boolean, Void, Object> {
    private ProgressDialog pd;

    /** application context. */
    public MyAsyn(Activity activity) {
        pd = new ProgressDialog(activity);
    }

    protected void onPreExecute() {
        pd.setMessage("Uploading.. Please wait");
        pd.show();
    }

    @Override
    protected String doInBackground(Boolean... urls) {

        pd.show();

        // do what you want to do in back ground

        try{
            Thread.sleep(4000);

        }catch(Exception e){};

        return null;
    }


    protected void onProgressUpdate(Integer values) {
        // TODO Auto-generated method stub

            // code to notify the progress
    }

    @Override
    protected void onPostExecute(Object result) {


        pd.dismiss();



    }
}


class uploadFileToServerTask extends AsyncTask<String, Integer , Object> {




    @Override
    protected Integer doInBackground(String... args) {
        try {
            String lineEnd = "\r\n";
            String twoHyphens = "--";
            String boundary = "*****";
            int bytesRead, bytesAvailable, bufferSize;
            byte[] buffer;
            @SuppressWarnings("PointlessArithmeticExpression")
            int maxBufferSize = 1 * 1024 * 1024;

            String UPLOAD_IMAGE_URL="http://ec2-35-162-68-34.us-west-2.compute.amazonaws.com:5000/abc";

            java.net.URL url = new URL(UPLOAD_IMAGE_URL);
            Log.d("URL", "url " + url);

            try {
                // Set your file path here
                FileInputStream fstrm = new FileInputStream(args[0]);

                // Set your server page url (and the file title/description)
                HttpFileUpload hfu = new HttpFileUpload(UPLOAD_IMAGE_URL, "Image","Image from android",args[0]);

                hfu.Send_Now(fstrm);

            } catch (FileNotFoundException e) {
                // Error: File not found
            }



            /*
            // Allow Inputs &amp; Outputs.
            connection.setDoInput(true);
            connection.setDoOutput(true);
            connection.setUseCaches(false);

            // Set HTTP method to POST.
            connection.setRequestMethod("POST");

            connection.setRequestProperty("Connection", "Keep-Alive");
            connection.setRequestProperty("Content-Type", "multipart/form-data;boundary=" + boundary);

            FileInputStream fileInputStream;
            DataOutputStream outputStream;
            {
                outputStream = new DataOutputStream(connection.getOutputStream());

                outputStream.writeBytes(twoHyphens + boundary + lineEnd);
                String filename = args[0];
                outputStream.writeBytes("Content-Disposition: form-data; name=\"file\";filename=\"" + filename + "\"" + lineEnd);
                outputStream.writeBytes(lineEnd);
                Log.d("File", "filename " + filename);

                fileInputStream = new FileInputStream(filename);

                bytesAvailable = fileInputStream.available();
                bufferSize = Math.min(bytesAvailable, maxBufferSize);

                buffer = new byte[bufferSize];

                // Read file
                bytesRead = fileInputStream.read(buffer, 0, bufferSize);

                while (bytesRead > 0) {
                    outputStream.write(buffer, 0, bufferSize);
                    bytesAvailable = fileInputStream.available();
                    bufferSize = Math.min(bytesAvailable, maxBufferSize);
                    bytesRead = fileInputStream.read(buffer, 0, bufferSize);
                }
                outputStream.writeBytes(lineEnd);
                outputStream.writeBytes(twoHyphens + boundary + twoHyphens + lineEnd);
            }

            int serverResponseCode = connection.getResponseCode();
            String serverResponseMessage = connection.getResponseMessage();
            Log.d("serverResponseCode", "" + serverResponseCode);
            Log.d("serverResponseMessage", "" + serverResponseMessage);

            fileInputStream.close();
            outputStream.flush();
            outputStream.close();

            if (serverResponseCode == 200) {
                return "true";
            }
        */
        } catch (Exception e) {
            e.printStackTrace();
        }
        return 1;
        // return "false";

    }

    @Override
    protected void onPostExecute(Object result) {

    }
}

