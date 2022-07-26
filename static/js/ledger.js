// function showAssets(){
//     var status = document.getElementById("calcgst");
//     var a = status.value
//     console.log(a);
//     if( a == "GST" ){
//         console.log(a);

//         document.getElementById('mtdcalc0').style.display = "flex";
//         document.getElementById('Approp0').style.display = "flex";
//     }
//     else{
        
//         document.getElementById('mtdcalc0').style.display = "none";
//         document.getElementById('Approp0').style.display = "none";
//     }
// }                     
                            
// function showbased(){
//     var status = document.getElementById("Approp");
//     var a = status.value
//     console.log(a);
//     if( a == "Services" ){
//         console.log(a);

//         document.getElementById('qlty').style.display = "none";
        
//     }
//     else{
//         document.getElementById('qlty').style.display = "flex";
        
//     }
// }

// function showname(){
    
//     var name = document.getElementById("name");
//     var mailingname = name.value;
//     document.getElementById("mailingname").value= mailingname;
// }

// function showunder(){
//     var status = document.getElementById("under");
//     var a = status.value;
//     console.log(a);
//     if( a == "BankAccount1" ){
//         console.log(a);

//         document.getElementById('bankac').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankdetails').style.display = "none";
//         document.getElementById('curntasts').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('bank2').style.display = "none";
//         document.getElementById('bank3').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
        
//     }

//     else if( a == "Bank_OCC_AC" ) {
        
//         document.getElementById('bankod').style.display = "flex";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('bankdetails').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('bank2').style.display = "none";
//         document.getElementById('bank3').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Bankod1" ) {
        
//         document.getElementById('bankod').style.display = "flex";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('bank2').style.display = "none";
//         document.getElementById('bank3').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "curntasts1" ) {
//         document.getElementById('roundmd20').style.display = "flex";
//         document.getElementById('Statutory_Details').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankdetails').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "dirctexpncs1" ) {
        
//         document.getElementById('direct_expences').style.display = "flex";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
    
//     else if( a == "dirctincome" ) {
        
//         document.getElementById('direct_expences').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "dutiesAndtax" ) {

//         document.getElementById('dutiesandtax1').style.display = "flex";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Expences_Direct" ) {
        
//         document.getElementById('direct_expences').style.display = "flex";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Expences_Inirect" ) {
        
//         document.getElementById('direct_expences').style.display = "flex";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Fixed_Assets" ) {

//         document.getElementById('dirctexpns4').style.display = "flex";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";

       
//     }
//     else if( a == "income_direct" ) {
        
//         document.getElementById('direct_expences').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "income_Indirect" ) {
        
//         document.getElementById('direct_expences').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Loans_liability" ) {
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Purchase_Account" ) {
//         document.getElementById('direct_expences').style.display = "flex";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Sales_Account" ) {
//         document.getElementById('direct_expences').style.display = "flex";
//         document.getElementById('applicablegst0').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Secured_loans" ) {
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Sundry_Creditors" ) {
//         document.getElementById('Sundry_commit').style.display = "flex";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }
//     else if( a == "Sundry_Debtors" ) {
//         document.getElementById('Sundry_commit').style.display = "flex";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
       
//     }

//     else if( a == "Unsecured_loans" ) {
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "flex";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('applicablegst0').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
//     }

//     else{
//         document.getElementById('Sundry_commit').style.display = "none";
//         document.getElementById('dirctexpns4').style.display = "none";
//         document.getElementById('direct_expences').style.display = "none";
//         document.getElementById('dutiesandtax1').style.display = "none";
//         document.getElementById('bankod').style.display = "none";
//         document.getElementById('bankac').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('bank2').style.display = "block";
//         document.getElementById('bank3').style.display = "flex";
//         document.getElementById('applicablegst0').style.display = "none";
       

//     }

// }

// function rounding(){
//     var status = document.getElementById("roundmd2");
//     var a = status.value
//     console.log(a);
//     if( a == "null" ){
//     console.log(a);
//     document.getElementById('rndlmt20').style.display = "none";



//     }
//     else{
//     document.getElementById('rndlmt20').style.display = "flex";
//     document.getElementById('valtyp0').style.display = "none";

//     }
// }    



// function showdirctexp2(){
//     var status = document.getElementById("typldr");
//     var a = status.value
//     console.log(a);
//     if( a == "Not_applicable" ){
//         console.log(a);

//         document.getElementById('dirctexpns2').style.display = "block";
//         document.getElementById('roundmd0').style.display = "none";
//         document.getElementById('rndlmt0').style.display = "none";
//     }
//     else if( a == "invroundg" ){
//         console.log(a);

//         document.getElementById('roundmd0').style.display = "block";
//         document.getElementById('rndlmt0').style.display = "block";
//         document.getElementById('dirctexpns2').style.display = "none";
        
//     }
//     else{
//         document.getElementById('dirctexpns2').style.display = "none";
//         document.getElementById('roundmd0').style.display = "none";
//         document.getElementById('rndlmt0').style.display = "none";
        
//     }
// }
// function showdirctexp3(){
//     var status = document.getElementById("applicablegst");
//     var a = status.value
//     console.log(a);
//     if( a == "Applicable" ){
//         console.log(a);

//         document.getElementById('stgst0').style.display = "block";
//         document.getElementById('typsofsply0').style.display = "block";
//         document.getElementById('calcgst0').style.display = "none";
        
//     }
//     else if( a == "Not_Applicable" ){
//         console.log(a);

//         document.getElementById('calcgst0').style.display = "block";
//         document.getElementById('stgst0').style.display = "none";
//         document.getElementById('typsofsply0').style.display = "none";
        
//     }
//     else if( a == "Undefined" ){
//         console.log(a);

//         document.getElementById('calcgst0').style.display = "none";
//         document.getElementById('stgst0').style.display = "block";
//         document.getElementById('typsofsply0').style.display = "block";
        
//     }

//     else{
//         document.getElementById('stgst0').style.display = "none";
//         document.getElementById('typsofsply0').style.display = "none";
//         document.getElementById('calcgst0').style.display = "none";
//     }
// }

// function showAssets2(){
//     var status = document.getElementById("calcgst2");
//     var a = status.value;
//     console.log(a);
//     if( a == "GST" ){
//         console.log(a);

//         document.getElementById('mtdcalc01').style.display = "flex";
//         document.getElementById('Approp01').style.display = "flex";
//     }
//     else{
        
//         document.getElementById('mtdcalc01').style.display = "none";
//         document.getElementById('Approp01').style.display = "none";
//     }
// }
                    
                    



// function showdutiesandtax2(){
//     var status = document.getElementById("typdty");
//     var a = status.value
//     console.log(a);
//     if( a == "gst" ){
//         console.log(a);
//         document.getElementById('taxtyp0').style.display = "flex";
//         document.getElementById('roundmd20').style.display = "flex";
//         document.getElementById('rndlmt20').style.display = "none";
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('prstgcalc0').style.display = "none";
//         document.getElementById('valtyp0').style.display = "none";
//     }
//     else if( a == "other" ){
//         console.log(a);

//         document.getElementById('prstgcalc0').style.display = "flex";
//         document.getElementById('Statutory_Details').style.display = "flex";
//         document.getElementById('taxtyp0').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('rndlmt20').style.display = "none";
//         document.getElementById('valtyp0').style.display = "none";
        
//     }
//     else{
//         document.getElementById('Statutory_Details').style.display = "none";
//         document.getElementById('prstgcalc0').style.display = "none";
//         document.getElementById('taxtyp0').style.display = "none";
//         document.getElementById('roundmd20').style.display = "none";
//         document.getElementById('rndlmt20').style.display = "none";
//         document.getElementById('valtyp0').style.display = "none";
        
        
//     }
// }


// function showdutiesandtax3(){
//     var status = document.getElementById("taxtyp");
//     var a = status.value
//     console.log(a);
//     if( a == "central" ){
//         console.log(a);

//         document.getElementById('prstgcalc0').style.display = "flex";
//         document.getElementById('valtyp0').style.display = "none";
        
//     }
//     else if( a == "cess" ){
//         console.log(a);

//         document.getElementById('valtyp0').style.display = "flex";
//         document.getElementById('prstgcalc0').style.display = "none";
      
        
//     }
//     else{
//         document.getElementById('valtyp0').style.display = "none";
//         document.getElementById('prstgcalc0').style.display = "none";
        
        
//     }
// }

// function showdutiesandtax4(){
//     var status = document.getElementById("valtyp");
//     var a = status.value
//     console.log(a);
//     if( a == "Based_on_Value" ){
//         console.log(a);

//         document.getElementById('prstgcalc0').style.display = "flex";
//         document.getElementById('rtprunit0').style.display = "none";
        
//     }
//     else if( a == "Based_on_Quntity" ){
//         console.log(a);

//         document.getElementById('rtprunit0').style.display = "flex";
//         document.getElementById('prstgcalc0').style.display = "none";
      
        
//     }
//     else if( a == "any" ){
//         console.log(a);
//         document.getElementById('prstgcalc0').style.display = "flex";
//         document.getElementById('rtprunit0').style.display = "none";
      
        
//     }
//     else{
//         document.getElementById('rtprunit0').style.display = "none";
//         document.getElementById('prstgcalc0').style.display = "none";
        
        
//     }
// }


                
// function showdirctexp4(){
//     var status = document.getElementById("applicablegst2");
//     var a = status.value
//     console.log(a);
//     console.log("hope");
//     if( a == "Applicable" ){
//         console.log(a);

//         document.getElementById('stgst20').style.display = "flex";
//         document.getElementById('typsofsply20').style.display = "flex";
        
        
//     }
//     else if( a == "Not_Applicable" ){
//         console.log(a);

        
//         document.getElementById('stgst20').style.display = "none";
//         document.getElementById('typsofsply20').style.display = "none";
        
//     }
//     else if( a == "Undefined" ){
//         console.log(a);

       
//         document.getElementById('stgst20').style.display = "none";
//         document.getElementById('typsofsply20').style.display = "flex";
        
//     }

//     else{
//         document.getElementById('stgst20').style.display = "none";
//         document.getElementById('typsofsply20').style.display = "none";
        
//     }
// }
 
// function bill(){
//     var status = document.getElementById("billbybill");
//     var a = status.value
//     console.log(a);
//     if( a == "Yes" ){
//         console.log(a);

//         document.getElementById('Default_Credit_period0').style.display = "flex";
//         document.getElementById('creditdays0').style.display = "flex";
//     }
//     else{
        
//         document.getElementById('Default_Credit_period0').style.display = "none";
//         document.getElementById('creditdays0').style.display = "none";
//     }
// }

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
        document.getElementById('bankod_a/c').style.display = "flex";
        document.getElementById('loans').style.display = "flex";
        document.getElementById('assets').style.display = "none"; 
        document.getElementById('account').style.display = "none";      
        document.getElementById('liabilities').style.display = "none";  
        document.getElementById('bill_by_bill').style.display = "none";  
        document.getElementById('statutory_details').style.display = "none";   
        document.getElementById('banka/c').style.display = "none";      
    }
    else if( a == "Bank_OD_A/c" ){
        document.getElementById('bankod_a/c').style.display = "flex";
        document.getElementById('loans').style.display = "flex";
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
   
function showdirctexp2(){
    var status = document.getElementById("typldr");
    var a = status.value
    console.log(a);
    if( a == "Not_applicable" ){
        console.log(a);

        document.getElementById('dirctexpns2').style.display = "block";
        document.getElementById('roundmd0').style.display = "none";
        document.getElementById('rndlmt0').style.display = "none";
    }
    else if( a == "invroundg" ){
        console.log(a);

        document.getElementById('roundmd0').style.display = "block";
        document.getElementById('rndlmt0').style.display = "block";
        document.getElementById('dirctexpns2').style.display = "none";
        
    }
    else{
        document.getElementById('dirctexpns2').style.display = "none";
        document.getElementById('roundmd0').style.display = "none";
        document.getElementById('rndlmt0').style.display = "none";
        
    }
}
function showdirctexp3(){
    var status = document.getElementById("applicablegst");
    var a = status.value
    console.log(a);
    if( a == "Applicable" ){
        console.log(a);

        document.getElementById('stgst0').style.display = "block";
        document.getElementById('typsofsply0').style.display = "block";
        document.getElementById('calcgst0').style.display = "none";
        
    }
    else if( a == "Not_Applicable" ){
        console.log(a);

        document.getElementById('calcgst0').style.display = "block";
        document.getElementById('stgst0').style.display = "none";
        document.getElementById('typsofsply0').style.display = "none";
        
    }
    else if( a == "Undefined" ){
        console.log(a);

        document.getElementById('calcgst0').style.display = "none";
        document.getElementById('stgst0').style.display = "block";
        document.getElementById('typsofsply0').style.display = "block";
        
    }

    else{
        document.getElementById('stgst0').style.display = "none";
        document.getElementById('typsofsply0').style.display = "none";
        document.getElementById('calcgst0').style.display = "none";
    }
}
                                      