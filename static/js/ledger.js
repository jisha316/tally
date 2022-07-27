

function showAssets(){
    var status = document.getElementById("call_gst");
    var a = status.value
    console.log(a);
    if( a == "GST" ){
        console.log(a);

        document.getElementById('appropriate_to').style.display = "flex";
        document.getElementById('method_of_calculation').style.display = "flex";
    }
    else{
        
        document.getElementById('appropriate_to').style.display = "none";
        document.getElementById('method_of_calculation').style.display = "none";
    }
}                     
                            
function showbased(){
    var status = document.getElementById("appropriate");
    var a = status.value
    console.log(a);
    if( a == "Services" ){
        console.log(a);

        document.getElementById('qlty').style.display = "none";
        
    }
    else{
        document.getElementById('qlty').style.display = "flex";
        
    }
}

function showunder(){
    var status = document.getElementById("under");
    var a = status.value;
    console.log(a);
    if( a == "Bank_Accounts" ){
        console.log(a);
        document.getElementById('banka/c').style.display = "flex";
        document.getElementById('assets').style.display = "flex";
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('statutory_details').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";     
    }
    else if( a == "Bank_OCC_AC" ){
        // document.getElementById('banka/c').style.display = "flex";
        // document.getElementById('bankod_a/c').style.display = "flex";
        // document.getElementById('bank_od_a/c').style.display = "flex";
        // document.getElementById('loans').style.display = "flex";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('account').style.display = "none";      
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";   
        document.getElementById('banka/c').style.display = "none";      
    }
    else if( a == "Bank_OD_A/c" ){
        // document.getElementById('banka/c').style.display = "flex";
        // document.getElementById('bankod_a/c').style.display = "flex";
        // document.getElementById('bank_od_a/c').style.display = "flex";
        // document.getElementById('loans').style.display = "flex";
        document.getElementById('assets').style.display = "none";
        document.getElementById('account').style.display = "none";      
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('banka/c').style.display = "none";      
    }
    else if( a == "Cash_in_Hand" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";       
    }
    else if( a == "Current_Assets" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";        
    }
    else if( a == "Deposits (Asset)" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none";   
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";    
    }
    else if( a == "Direct_Expenses" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";        
    }
    else if( a == "Direct_Incomes" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";          
    }
    else if( a == "Duties_and_Taxes" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";          
    }
    else if( a == "Expences_Direct" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";         
    }
    else if( a == "Expences_Indirect" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";         
    }
    else if( a == "Fixed_Assets" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";         
    }
    else if( a == "Income_direct" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";         
    }
    else if( a == "Income_Indirect" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";         
    }
    else if( a == "Loans_Advance" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('loans').style.display = "none";  
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";    
    }
    else if( a == "Loans_liability" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";        
    }
    else if( a == "Provisions" ){
        document.getElementById('liabilities').style.display = "flex";
        document.getElementById('assets').style.display = "none";
        document.getElementById('loans').style.display = "none";          
        document.getElementById('account').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('statutory_details').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";      
    }
    else if( a == "Purchase_Account" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";         
    }
    else if( a == "Reserves_&_Surplus" ){
        document.getElementById('account').style.display = "flex";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none";
        document.getElementById('loans').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('statutory_details').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";      
    }
    else if( a == "Retained" ){
        document.getElementById('account').style.display = "flex";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none";
        document.getElementById('loans').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";       
    }
    else if( a == "Sales_Account" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";          
    }
    else if( a == "Secured_loans" ){
        document.getElementById('loans').style.display = "flex";   
        document.getElementById('statutory_details').style.display = "flex";   
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";          
    }
    else if( a == "Stock" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('loans').style.display = "none";  
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";     
    }
    else if( a == "Sundry_Creditors" ){
        document.getElementById('liabilities').style.display = "flex";
        document.getElementById('bill_by_bill').style.display = "flex";
        document.getElementById('assets').style.display = "none";
        document.getElementById('loans').style.display = "none";          
        document.getElementById('account').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";        
    }
    else if( a == "Sundry_Debtors" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('bill_by_bill').style.display = "flex";
        document.getElementById('loans').style.display = "none";  
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";      
    }
    else if( a == "Unsecured_loans" ){
        document.getElementById('loans').style.display = "flex";          
        document.getElementById('statutory_details').style.display = "flex";          
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none";
        document.getElementById('account').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";          
    }
    else{
        document.getElementById('assets').style.display = "none";
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('account').style.display = "none";      
        document.getElementById('bill_by_bill').style.display = "none";   
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";   
    }
}

function bill(){
    var status = document.getElementById("billbybill");
    var a = status.value
    console.log(a);
    if( a == "Yes" ){
        console.log(a);

        document.getElementById('credit_period').style.display = "flex";
        document.getElementById('voucher_enter').style.display = "flex";
    }
    else{
        
        document.getElementById('credit_period').style.display = "none";
        document.getElementById('voucher_enter').style.display = "none";
    }
}
   

                                      