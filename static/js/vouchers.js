function showVoucherType(){
    var status = document.getElementById("voucher_type");
    var a = status.value;
    console.log(a);
    if( a == "Abr" ){
        console.log(a);

        document.getElementById('provide').style.display = "flex";
        document.getElementById('abr').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('enable').style.display = "none";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
        

    }
    else if( a == "Attendance" ){
        
        document.getElementById('provide').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('abr').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('enable').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('attd').style.display = "flex";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
        
        
    }
    else if( a == "Contra" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('abr').style.display = "none";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('contra').style.display = "flex";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
        
        
    }
    else if( a == "Credit_Note" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "flex";
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('abr').style.display = "none";
        document.getElementById('track').style.display = "none";
        // document.getElementById('credit_note').style.display = "flex";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
       
        
    }
    else if( a == "Debit_Note" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('abr').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('attd').style.display = "none";
        // document.getElementById('debit_note').style.display = "flex";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('attd').style.display = "none"; 
        // document.getElementById('delivery_note').style.display = "none";   
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
       
        
    }
    else if( a == "Delivery_Note" ){
        document.getElementById('enable').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "flex";
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('provide').style.display = "none";
        document.getElementById('abr').style.display = "none";
        // document.getElementById('delivery_note').style.display = "flex";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
        
       
        
    }
    else if( a == "Job_Work_In_Order" ){
        
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('set/alter').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('provide').style.display = "none"; 
        document.getElementById('abr').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        // document.getElementById('job_work_in').style.display = "flex";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
        

        
    }
    else if( a == "Job_Work_Out_Order" ){
        
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('set/alter').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('provide').style.display = "none"; 
        document.getElementById('abr').style.display = "none";
        document.getElementById('enable').style.display = "none";
        // document.getElementById('job_work_out').style.display = "flex";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
        
        
    }
    else if( a == "Journal" ){
        
        document.getElementById('provide').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('abr').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('enable').style.display = "none";
        // document.getElementById('journal').style.display = "flex";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";  
        // document.getElementById('material_in').style.display = "none"; 
        // document.getElementById('material_out').style.display = "none"; 
        
    }
    else if( a == "Material_In" ){
        // document.getElementById('material_in').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('provide').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('abr').style.display = "none";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none"; 
       
    }
    else if( a == "Material_Out" ){
        // document.getElementById('material_out').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('provide').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('abr').style.display = "none";
        document.getElementById('title_print').style.display = "none"; 
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('enable').style.display = "none";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";
          
        
       
    }
    else if( a == "memorandum" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('optional').style.display = "none";
        document.getElementById('abr').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        // document.getElementById('attd').style.display = "none";
        // document.getElementById('material_out').style.display = "none";
        // document.getElementById('jurisdiction').style.display = "none";
        // document.getElementById('material_in').style.display = "none";
        // document.getElementById('journal').style.display = "none";
        // document.getElementById('contra').style.display = "none";
        // document.getElementById('credit_note').style.display = "none";
        // document.getElementById('debit_note').style.display = "none";
        // document.getElementById('delivery_note').style.display = "none";
        // document.getElementById('job_work_in').style.display = "none";
        // document.getElementById('job_work_out').style.display = "none";   
       
    }
    
    
    
}