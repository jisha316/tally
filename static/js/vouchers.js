function showVoucherNo(){
    var status = document.getElementById("voucher_no");
    var a = status.value;
    console.log(a);
    if( a == "option" ){
        console.log(a);

        document.getElementById('advanced').style.display = "none";
        document.getElementById('duplicates').style.display = "none";
    }
    else if( a == "Automatic" ){
        document.getElementById('advanced').style.display = "flex";
        document.getElementById('duplicates').style.display = "none";
    }
    else if( a == "Override" ){
        document.getElementById('advanced').style.display = "flex";
        document.getElementById('duplicates').style.display = "flex";
    }
    else if( a == "Manual" ){
        document.getElementById('duplicates').style.display = "flex";
        document.getElementById('advanced').style.display = "none";
    }
    else if( a == "Multiuser Auto" ){
        document.getElementById('advanced').style.display = "flex";
        document.getElementById('duplicates').style.display = "none";
    }
    else{
        document.getElementById('duplicates').style.display = "none";
        document.getElementById('advanced').style.display = "none";
    }
}

function showVoucherType(){
    var val=document.getElementById("voucher_type").value;
        if(val=="Attendance")
        {
            newval="Attd";
        }
        else if(val=="Contra")
        {
            newval="Ctra";
        }
        else if(val=="Credit_Note")
        {
            newval="C/Note";
        }
        else if(val=="Debit_Note")
        {
            newval="D/Note";
        }
        else if(val=="Delivery_Note")
        {
            newval="Dely Note";
        }
        else if(val=="Job_Work_In_Order")
        {
            newval="Job Wrk In Ordr";
        }
        else if(val=="Job_Work_Out_Order")
        {
            newval="Job Wrk Out Ordr";
        }
        else if(val=="Journal")
        {
            newval="Jrnl";
        }
        else if(val=="Material_In")
        {
            newval="Mat In";
        }
        else if(val=="Material_Out")
        {
            newval="Mat Out";
        }
        else if(val=="Memorandum")
        {
            newval="Memo";
        }
        else if(val=="Payment")
        {
            newval="Pymt";
        }
        else if(val=="Payroll")
        {
            newval="Pyrl";
        }
        else if(val=="Physical_Stock")
        {
            newval="Phy Stk";
        }
        else if(val=="Purchase")
        {
            newval="Purc";
        }
        else if(val=="Purchase_Order")
        {
            newval="Purc Order";
        }
        else if(val=="Receipt")
        {
            newval="Rcpt";
        }
        else if(val=="Receipt_Note")
        {
            newval="Rcpt Note";
        }
        else if(val=="Rejections_In")
        {
            newval="Rej In";
        }
        else if(val=="Rejections_Out")
        {
            newval="Rej Out";
        }
        else if(val=="Reversing_Journal")
        {
            newval="Rev Jrnl";
        }
        else if(val=="Sales")
        {
            newval="Sale";
        }
        else if(val=="Sales_Order")
        {
            newval="Sales Ordr";
        }
        else if(val=="Stock_Journal")
        {
            newval="Stk Jrnl";
        }
        else
        {
            newval="";
        }
        document.getElementById("abr").value = newval;
    
    var status = document.getElementById("voucher_type");
    var a = status.value;
    console.log(a);
    if( a == "Attendance" ){
        console.log(a);
        
        document.getElementById('provide').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Contra" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Credit_Note" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "flex";
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Debit_Note" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('attd').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";   
    }
    else if( a == "Delivery_Note" ){
        document.getElementById('enable').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "flex";
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('provide').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";    
    }
    else if( a == "Job_Work_In_Order" ){
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('set/alter').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('provide').style.display = "none"; 
        document.getElementById('enable').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";    
    }
    else if( a == "Job_Work_Out_Order" ){
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('set/alter').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('provide').style.display = "none"; 
        document.getElementById('enable').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Journal" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";    
    }
    else if( a == "Material_In" ){
        document.getElementById('optional').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('provide').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Material_Out" ){
        document.getElementById('optional').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('provide').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('title_print').style.display = "none"; 
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";   
    }
    else if( a == "Memorandum" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('optional').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
        
       
    }
    else if( a == "Payment" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Payroll" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Physical_Stock" ){
        document.getElementById('track').style.display = "flex";
        document.getElementById('provide').style.display = "none";
        document.getElementById('optional').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Purchase" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Purchase_Order" ){
        
        document.getElementById('optional').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('provide').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Receipt" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Receipt_Note" ){
        document.getElementById('optional').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('provide').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Rejections_In" ){
        document.getElementById('optional').style.display = "flex";
        document.getElementById('provide').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Rejections_Out" ){
        document.getElementById('optional').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('provide').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Reversing_Journal" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('optional').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('journal').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }
    else if( a == "Sales" ){
        document.getElementById('provide').style.display = "flex";
        document.getElementById('optional').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('pos').style.display = "flex";
        document.getElementById('bank').style.display = "flex";
        document.getElementById('title_print').style.display = "flex";
        document.getElementById('jurisdiction').style.display = "flex";
        document.getElementById('set/alter').style.display = "flex";
        document.getElementById('track').style.display = "none";
        document.getElementById('journal').style.display = "none";
    }
    else if( a == "Sales_Order" ){
        document.getElementById('optional').style.display = "flex";
        document.getElementById('enable').style.display = "flex";
        document.getElementById('set/alter').style.display = "flex";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
        document.getElementById('provide').style.display = "none";
        document.getElementById('track').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        
        document.getElementById('journal').style.display = "none";  
    }
    else if( a == "Stock_Journal" ){
        document.getElementById('optional').style.display = "flex";
        document.getElementById('journal').style.display = "flex";
        document.getElementById('track').style.display = "flex";
        document.getElementById('provide').style.display = "none";
        document.getElementById('enable').style.display = "none";
        document.getElementById('title_print').style.display = "none";
        document.getElementById('jurisdiction').style.display = "none";
        document.getElementById('set/alter').style.display = "none";
        document.getElementById('pos').style.display = "none";
        document.getElementById('bank').style.display = "none";
    }    
}

function showPOS(){
    var status = document.getElementById("POS");
    var a = status.value;
    console.log(a);
    if( a == "Yes" ){
        console.log(a);

        document.getElementById('msg_1').style.display = "flex";
        document.getElementById('msg_2').style.display = "flex";
    }
    else{
        document.getElementById('msg_1').style.display = "none";
        document.getElementById('msg_2').style.display = "none";
    }
}