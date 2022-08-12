function showname(){      
    var name = document.getElementById("name");
    var mailingname = name.value;
    document.getElementById("mailingname").value= mailingname;
}

function showunder(){
    var status = document.getElementById("under");
    var a = status.value;
    console.log(a);
    if( a == "Bank_Accounts" ){
        console.log(a);
        
        document.getElementById('assets').style.display = "flex";
        document.getElementById('banka/c').style.display = "flex"; 
        document.getElementById('sd').style.display = "none"; 
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('bank_details').style.display = "none"; 
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Bank_OCC_AC" ){
        document.getElementById('loans').style.display = "flex";
        document.getElementById('bankod_a/c').style.display = "flex";
        document.getElementById('banka/c').style.display = "flex";  
        document.getElementById('bank_details').style.display = "none";
        document.getElementById('sd').style.display = "none"; 
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('account').style.display = "none";      
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";    
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none";  
        document.getElementById('rounding_method').style.display = "none";    
    }
    else if( a == "Bank_OD_A/c" ){
        document.getElementById('loans').style.display = "flex";
        document.getElementById('bankod_a/c').style.display = "flex";
        document.getElementById('banka/c').style.display = "flex"; 
        document.getElementById('sd').style.display = "none"; 
        document.getElementById('bank_details').style.display = "none";
        document.getElementById('assets').style.display = "none";
        document.getElementById('account').style.display = "none";      
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('statutory_details').style.display = "none";   
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    
    else if( a == "Cash_in_Hand" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none"; 
        document.getElementById('sd').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";   
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Current_Assets" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('sd_4').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";    
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Deposits (Asset)" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('account').style.display = "none";   
        document.getElementById('sd').style.display = "none";   
        document.getElementById('liabilities').style.display = "none";   
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";  
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";   
    }
    else if( a == "Direct_Expenses" ){ 
        document.getElementById('Type_of_ledger').style.display = "flex";  
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";    
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Direct_Incomes" ){ 
        document.getElementById('Type_of_ledger').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";  
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";         
    }
    else if( a == "Duties_and_Taxes" ){ 
        document.getElementById('liabilities').style.display = "flex";
        document.getElementById('Duties&Taxes').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";     
        document.getElementById('account').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none";          
    }
    else if( a == "Expences_Direct" ){ 
        document.getElementById('Type_of_ledger').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";         
    }
    else if( a == "Expences_Indirect" ){ 
        document.getElementById('Type_of_ledger').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";         
    }
    else if( a == "Fixed_Assets" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('sd_1').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";  
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";        
    }
    else if( a == "Income_direct" ){ 
        document.getElementById('Type_of_ledger').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";         
    }
    else if( a == "Income_Indirect" ){ 
        document.getElementById('Type_of_ledger').style.display = "flex";  
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";          
    }
    else if( a == "Loans_Advance" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";  
        document.getElementById('account').style.display = "none";  
        document.getElementById('sd').style.display = "none";    
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Loans_liability" ){ 
        document.getElementById('statutory_details').style.display = "flex"; 
        document.getElementById('sd_4').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";     
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";    
    }
    else if( a == "Provisions" ){
        document.getElementById('liabilities').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('assets').style.display = "none";
        document.getElementById('sd').style.display = "none"; 
        document.getElementById('loans').style.display = "none";          
        document.getElementById('account').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('statutory_details').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";      
    }
    else if( a == "Purchase_Account" ){ 
        document.getElementById('Type_of_ledger').style.display = "flex";  
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('mailing_details').style.display = "none";    
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Duties&Taxes').style.display = "none";  
        document.getElementById('rounding_method').style.display = "none";         
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
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";   
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
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Sales_Account" ){ 
        document.getElementById('Type_of_ledger').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";    
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";          
    }
    else if( a == "Secured_loans" ){
        document.getElementById('loans').style.display = "flex";   
        document.getElementById('statutory_details').style.display = "flex";   
        document.getElementById('sd_4').style.display = "flex"; 
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('account').style.display = "none";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";      
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Stock" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";  
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none"; 
        document.getElementById('sd').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Sundry_Creditors" ){
        document.getElementById('liabilities').style.display = "flex";
        document.getElementById('bill_by_bill').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('assets').style.display = "none";
        document.getElementById('loans').style.display = "none";          
        document.getElementById('account').style.display = "none";  
        document.getElementById('sd').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";    
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";     
    }
    else if( a == "Sundry_Debtors" ){
        document.getElementById('assets').style.display = "flex";
        document.getElementById('bill_by_bill').style.display = "flex";
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('loans').style.display = "none";  
        document.getElementById('account').style.display = "none";     
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('sd').style.display = "none"; 
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";   
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";    
    }
    else if( a == "Unsecured_loans" ){
        document.getElementById('loans').style.display = "flex";          
        document.getElementById('statutory_details').style.display = "flex";  
        document.getElementById('sd_4').style.display = "flex";         
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('liabilities').style.display = "none";
        document.getElementById('assets').style.display = "none";
        document.getElementById('account').style.display = "none"; 
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none"; 
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none";          
    }
    else{
        document.getElementById('bank_details').style.display = "flex";
        document.getElementById('mailing_details').style.display = "flex";
        document.getElementById('Duties&Taxes').style.display = "none"; 
        document.getElementById('Type_of_ledger').style.display = "none"; 
        document.getElementById('rounding_method').style.display = "none"; 
        document.getElementById('assets').style.display = "none";
        document.getElementById('loans').style.display = "none"; 
        document.getElementById('liabilities').style.display = "none";   
        document.getElementById('account').style.display = "none";      
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('sd').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('sd_4').style.display = "none";
        document.getElementById('sd_1').style.display = "none";
        document.getElementById('sd_3').style.display = "none";
        document.getElementById('sd_3').style.display = "none";
        document.getElementById('banka/c').style.display = "none"; 
        document.getElementById('bankod_a/c').style.display = "none";   
    }
}
function typ_ledger(){
    var status = document.getElementById("typledger");
    var a = status.value
    console.log(a);
    if( a == "Not_Applicable" ){
        console.log(a);
        
        document.getElementById('sd_1').style.display = "flex"; 
        document.getElementById('statutory_details').style.display = "flex";    
        document.getElementById('rounding_method1').style.display = "none";    
    }
    else if ( a == "Discount" ){
        document.getElementById('sd_1').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";  
        document.getElementById('rounding_method1').style.display = "none"; 
        document.getElementById('sd_2').style.display = "none";
        document.getElementById('sd_3').style.display = "none"; 
        document.getElementById('sd_4').style.display = "none"; 
        document.getElementById('appropriate_to').style.display = "none"; 
        document.getElementById('method_of_calculation').style.display = "none"; 
    }
    else if( a == "Invoice_Rounding" ){
        document.getElementById('sd_1').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('rounding_method1').style.display = "flex"; 
        document.getElementById('sd_2').style.display = "none";
        document.getElementById('sd_3').style.display = "none"; 
        document.getElementById('sd_4').style.display = "none"; 
        document.getElementById('appropriate_to').style.display = "none"; 
        document.getElementById('method_of_calculation').style.display = "none"; 
    }
    else{ 
        document.getElementById('sd_1').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('rounding_method1').style.display = "none"; 
        document.getElementById('sd_2').style.display = "none";
        document.getElementById('sd_3').style.display = "none"; 
        document.getElementById('sd_4').style.display = "none"; 
        document.getElementById('appropriate_to').style.display = "none"; 
        document.getElementById('method_of_calculation').style.display = "none"; 
    }
}
function typ_dttax(){
    var status = document.getElementById("type_duty_tax");
    var a = status.value
    console.log(a);
    if( a == "Others" ){
        console.log(a);
        
        document.getElementById('perc_calc').style.display = "flex"; 
        document.getElementById('statutory_details').style.display = "flex";
        document.getElementById('sd_4').style.display = "flex"; 
        document.getElementById('rate_per_unit').style.display = "none"; 
        document.getElementById('val_type').style.display = "none";  
        document.getElementById('tax_type').style.display = "none";
        document.getElementById('rounding_method').style.display = "none";
        document.getElementById('rounding_limit').style.display = "none";
    }
    else if( a == "GST" ){
        document.getElementById('tax_type').style.display = "flex";
        document.getElementById('perc_calc').style.display = "flex"; 
        document.getElementById('rounding_method').style.display = "flex"; 
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('sd_4').style.display = "none"; 
        document.getElementById('appropriate_to').style.display = "none"; 
        document.getElementById('method_of_calculation').style.display = "none"; 
    }
    else{
        document.getElementById('tax_type').style.display = "none";
        document.getElementById('perc_calc').style.display = "none"; 
        document.getElementById('statutory_details').style.display = "none";
        document.getElementById('rounding_method').style.display = "none";
        document.getElementById('sd_4').style.display = "none"; 
        document.getElementById('appropriate_to').style.display = "none"; 
        document.getElementById('method_of_calculation').style.display = "none"; 
    }
}
function round_mthd(){
    var status = document.getElementById("rond_met");
    var a = status.value
    console.log(a);
    if( a == "Not_Applicable" ){
        console.log(a);
        
        document.getElementById('rounding_limit').style.display = "none";     
    }
    else{
        
        document.getElementById('rounding_limit').style.display = "flex"; 
    }
}
function tax_type0(){
    var status = document.getElementById("taxtype");
    var a = status.value
    console.log(a);
    if( a == "Central_Tax" ){
        console.log(a);
        
        document.getElementById('val_type').style.display = "none";     
    }
    else if( a == "Cess" ){
        
        document.getElementById('val_type').style.display = "flex"; 
    }
    else if( a == "Integrated_Tax" ){
        document.getElementById('val_type').style.display = "none"; 
    }
    else if( a == "State_Tax" ){
        document.getElementById('val_type').style.display = "none"; 
    }
    else{
        document.getElementById('perc_calc').style.display = "none";
        document.getElementById('val_type').style.display = "none"; 
    }
}
function valtype0(){
    var status = document.getElementById("valtype");
    var a = status.value
    console.log(a);
    if( a == "Any" ){
        console.log(a);
        
        document.getElementById('perc_calc').style.display = "flex";
        document.getElementById('rate_per_unit').style.display = "none";     
    }
    else if( a == "Based_on_Quantity" ){
        document.getElementById('rate_per_unit').style.display = "flex";
        document.getElementById('perc_calc').style.display = "none";
    }
    else if( a == "Based_on_Value" ){
        document.getElementById('perc_calc').style.display = "flex";
        document.getElementById('rate_per_unit').style.display = "none"; 
    }
    else{
        document.getElementById('perc_calc').style.display = "none";
        document.getElementById('rate_per_unit').style.display = "none"; 
    }
}
function showgstA(){
    var status = document.getElementById("gst_applicable");
    var a = status.value
    console.log(a);
    if( a == "Not_Applicable" ){
        console.log(a);

        document.getElementById('sd_4').style.display = "flex";
        document.getElementById('sd_3').style.display = "none";
        document.getElementById('sd_2').style.display = "none";
    }
    else if( a == "Applicable" ){
        document.getElementById('sd_2').style.display = "flex";
        document.getElementById('sd_3').style.display = "flex";
        document.getElementById('sd_4').style.display = "none";
        document.getElementById('appropriate_to').style.display = "none"; 
        document.getElementById('method_of_calculation').style.display = "none"; 
    }
    else if( a == "Undifined" ){
        document.getElementById('sd_3').style.display = "flex";
        document.getElementById('sd_2').style.display = "none";
        document.getElementById('sd_4').style.display = "none";
        document.getElementById('appropriate_to').style.display = "none"; 
        document.getElementById('method_of_calculation').style.display = "none"; 
    }
    else{
        document.getElementById('sd_2').style.display = "none";
        document.getElementById('sd_3').style.display = "none";
        document.getElementById('sd_4').style.display = "none";
        document.getElementById('appropriate_to').style.display = "none"; 
        document.getElementById('method_of_calculation').style.display = "none"; 
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