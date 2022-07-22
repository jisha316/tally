function showAssets(){
    var status = document.getElementById("calcgst");
    var a = status.value
    console.log(a);
    if( a == "GST" ){
        console.log(a);

        document.getElementById('mtdcalc0').style.display = "flex";
        document.getElementById('Approp0').style.display = "flex";
    }
    else{
        
        document.getElementById('mtdcalc0').style.display = "none";
        document.getElementById('Approp0').style.display = "none";
    }
}                     
                            
function showbased(){
    var status = document.getElementById("Approp");
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

function showname(){
    
    var name = document.getElementById("name");
    var mailingname = name.value;
    document.getElementById("mailingname").value= mailingname;
}

function showunder(){
    var status = document.getElementById("under");
    var a = status.value;
    console.log(a);
    if( a == "BankAccount1" ){
        console.log(a);

        document.getElementById('bankac').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankdetails').style.display = "none";
        document.getElementById('curntasts').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('bank2').style.display = "none";
        document.getElementById('bank3').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
        
    }

    else if( a == "Bank_OCC_AC" ) {
        
        document.getElementById('bankod').style.display = "flex";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('bankdetails').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('bank2').style.display = "none";
        document.getElementById('bank3').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Bankod1" ) {
        
        document.getElementById('bankod').style.display = "flex";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('bank2').style.display = "none";
        document.getElementById('bank3').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "curntasts1" ) {
        document.getElementById('roundmd20').style.display = "flex";
        document.getElementById('Statutory_Details').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankdetails').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "dirctexpncs1" ) {
        
        document.getElementById('direct_expences').style.display = "flex";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    
    else if( a == "dirctincome" ) {
        
        document.getElementById('direct_expences').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "dutiesAndtax" ) {

        document.getElementById('dutiesandtax1').style.display = "flex";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Expences_Direct" ) {
        
        document.getElementById('direct_expences').style.display = "flex";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Expences_Inirect" ) {
        
        document.getElementById('direct_expences').style.display = "flex";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Fixed_Assets" ) {

        document.getElementById('dirctexpns4').style.display = "flex";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";

       
    }
    else if( a == "income_direct" ) {
        
        document.getElementById('direct_expences').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "income_Indirect" ) {
        
        document.getElementById('direct_expences').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Loans_liability" ) {
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Purchase_Account" ) {
        document.getElementById('direct_expences').style.display = "flex";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Sales_Account" ) {
        document.getElementById('direct_expences').style.display = "flex";
        document.getElementById('applicablegst0').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Secured_loans" ) {
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Sundry_Creditors" ) {
        document.getElementById('Sundry_commit').style.display = "flex";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }
    else if( a == "Sundry_Debtors" ) {
        document.getElementById('Sundry_commit').style.display = "flex";
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
       
    }

    else if( a == "Unsecured_loans" ) {
        document.getElementById('roundmd20').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "flex";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('applicablegst0').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
    }

    else{
        document.getElementById('Sundry_commit').style.display = "none";
        document.getElementById('dirctexpns4').style.display = "none";
        document.getElementById('direct_expences').style.display = "none";
        document.getElementById('dutiesandtax1').style.display = "none";
        document.getElementById('bankod').style.display = "none";
        document.getElementById('bankac').style.display = "none";
        document.getElementById('Statutory_Details').style.display = "none";
        document.getElementById('bank2').style.display = "block";
        document.getElementById('bank3').style.display = "flex";
        document.getElementById('applicablegst0').style.display = "none";
       

    }

}

function rounding(){
    var status = document.getElementById("roundmd2");
    var a = status.value
    console.log(a);
    if( a == "null" ){
    console.log(a);
    document.getElementById('rndlmt20').style.display = "none";



    }
    else{
    document.getElementById('rndlmt20').style.display = "flex";
    document.getElementById('valtyp0').style.display = "none";

    }
}    

//  <=====================================================>
//                     
//  <=====================================================>

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

function showAssets2(){
    var status = document.getElementById("calcgst2");
    var a = status.value;
    console.log(a);
    if( a == "GST" ){
        console.log(a);

        document.getElementById('mtdcalc01').style.display = "flex";
        document.getElementById('Approp01').style.display = "flex";
    }
    else{
        
        document.getElementById('mtdcalc01').style.display = "none";
        document.getElementById('Approp01').style.display = "none";
    }
}
                    
                    
// <============================================================>

// <=============================================================>


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

// <=======================================================>

// <=======================================================>
                
function showdirctexp4(){
    var status = document.getElementById("applicablegst2");
    var a = status.value
    console.log(a);
    console.log("hope");
    if( a == "Applicable" ){
        console.log(a);

        document.getElementById('stgst20').style.display = "flex";
        document.getElementById('typsofsply20').style.display = "flex";
        
        
    }
    else if( a == "Not_Applicable" ){
        console.log(a);

        
        document.getElementById('stgst20').style.display = "none";
        document.getElementById('typsofsply20').style.display = "none";
        
    }
    else if( a == "Undefined" ){
        console.log(a);

       
        document.getElementById('stgst20').style.display = "none";
        document.getElementById('typsofsply20').style.display = "flex";
        
    }

    else{
        document.getElementById('stgst20').style.display = "none";
        document.getElementById('typsofsply20').style.display = "none";
        
    }
}


// <========================================================>
//                 Bill
// <========================================================>
  
function bill(){
    var status = document.getElementById("billbybill");
    var a = status.value
    console.log(a);
    if( a == "Yes" ){
        console.log(a);

        document.getElementById('Default_Credit_period0').style.display = "flex";
        document.getElementById('creditdays0').style.display = "flex";
    }
    else{
        
        document.getElementById('Default_Credit_period0').style.display = "none";
        document.getElementById('creditdays0').style.display = "none";
    }
}
                                      