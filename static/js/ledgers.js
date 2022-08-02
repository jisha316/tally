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

function showdutiesandtax2(){
    var status = document.getElementById("typdty");
    var a = status.value
    console.log(a);
    if( a == "gst" ){
        console.log(a);
        document.getElementById('taxtyp0').style.display = "flex";
        document.getElementById('roundmd20').style.display = "flex";
        document.getElementById('rndlmt20').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('prstgcalc0').style.display = "none";
        document.getElementById('valtyp0').style.display = "none";
    }
    else if( a == "other" ){
        console.log(a);

        document.getElementById('prstgcalc0').style.display = "flex";
        document.getElementById('Statutory_Details').style.display = "flex";
        document.getElementById('taxtyp0').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('rndlmt20').style.display = "none";
        document.getElementById('valtyp0').style.display = "none";    
    }
    else{
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('prstgcalc0').style.display = "none";
        document.getElementById('taxtyp0').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('rndlmt20').style.display = "none";
        document.getElementById('valtyp0').style.display = "none";    
    }
    }

    function showdutiesandtax3(){
    var status = document.getElementById("taxtyp");
    var a = status.value
    console.log(a);
    if( a == "central" ){
        console.log(a);

        document.getElementById('prstgcalc0').style.display = "flex";
        document.getElementById('valtyp0').style.display = "none";     
    }
    else if( a == "cess" ){
        console.log(a);

        document.getElementById('valtyp0').style.display = "flex";
        document.getElementById('prstgcalc0').style.display = "none";    
    }
    else{
        document.getElementById('valtyp0').style.display = "none";
        document.getElementById('prstgcalc0').style.display = "none";         
    }
    }

    function showdutiesandtax4(){
    var status = document.getElementById("valtyp");
    var a = status.value
    console.log(a);
    if( a == "Based_on_Value" ){
        console.log(a);

        document.getElementById('prstgcalc0').style.display = "flex";
        document.getElementById('rtprunit0').style.display = "none";    
    }
    else if( a == "Based_on_Quntity" ){
        console.log(a);

        document.getElementById('rtprunit0').style.display = "flex";
        document.getElementById('prstgcalc0').style.display = "none";    
    }
    else if( a == "any" ){
        console.log(a);
        document.getElementById('prstgcalc0').style.display = "flex";
        document.getElementById('rtprunit0').style.display = "none";    
    }
    else{
        document.getElementById('rtprunit0').style.display = "none";
        document.getElementById('prstgcalc0').style.display = "none";    
    }
}

function showunder(){
    var status = document.getElementById("under");
    var a = status.value;
    console.log(a);
    if( a == "Bank_Accounts" ){
        console.log(a);
        
        document.getElementById('assets').style.display = "flex";
        document.getElementById('banka/c').style.display = "flex"; 
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('bank_details').style.display = "none"; 
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";      
    }
    else if( a == "Bank_OCC_AC" ){
        document.getElementById('loans').style.display = "flex";
        document.getElementById('bankod_a/c').style.display = "flex";
        document.getElementById('banka/c').style.display = "flex";  
        document.getElementById('bank_details').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('account').style.display = "none";      
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";       
    }
    else if( a == "Bank_OD_A/c" ){
        document.getElementById('loans').style.display = "flex";
        document.getElementById('bankod_a/c').style.display = "flex";
        document.getElementById('banka/c').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "none";
        document.getElementById('assets').style.display = "none";
        document.getElementById('account').style.display = "none";      
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('statutory_details').style.display = "none";       
    }
    else if( a == "Cash_in_Hand" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";          
    }
    else if( a == "Duties_and_Taxes" ){ 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('dutiesandtax1').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";          
    }
    else if( a == "Stock" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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
        document.getElementById('bank_details').style.display = "flex";
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