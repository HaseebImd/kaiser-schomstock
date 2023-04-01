var city = document.getElementById('city')
var category = document.getElementById('category')
var postingTitle = document.getElementById('postingtitle')
var postalCode = document.getElementById('postalcode')
var postBody   =document.getElementById('full-featured')
var jobTitle = document.getElementById('jobTitle')
var compensation = document.getElementById('compensation')
var emailAddress = document.getElementById('emailAddress')
var submitBtn = document.getElementById('submitBtn')



function CheckRequiredFields()
{
    if(city.value=='')
    {
        ShowToastMessage('Please provide City name')
    }
    else if(category.value=='')
    {
        ShowToastMessage('Please provide Category name')
    }
    else if (postingTitle.value == '')
    {
        ShowToastMessage('Please provide Posting Title')    
    }
    else if (postalCode.value == '')
    {
        ShowToastMessage('Please provide Postal Code')    
    }
    else if (postBody.value == '')
    {
        ShowToastMessage('Please provide Post Body')    
    }
    else if (jobTitle.value == '')
    {
        ShowToastMessage('Please provide Job Title')    
    }
    else if (compensation.value == '')
    {
        ShowToastMessage('Please provide Compensation')    
    }
    else if (emailAddress.value == '')
    {
        ShowToastMessage('Please provide Email Address')    
    }
    else
    {
        submitBtn.click
    }
}


function ShowToastMessage(message)
{
    document.getElementById("toastBody").innerHTML = message;
    document.getElementById("toastbtn").click();
}