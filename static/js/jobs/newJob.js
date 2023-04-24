var city = document.getElementById('city')
var category = document.getElementById('category')
var postingTitle = document.getElementById('postingtitle')
var postalCode = document.getElementById('postalcode')
var postBody   =document.getElementById('full-featured')
var jobTitle = document.getElementById('jobTitle')
var compensation = document.getElementById('compensation')
var employementType = document.getElementById('employementType')
var emailAddress = document.getElementById('emailAddress')
var submitBtn = document.getElementById('submitBtn')

var allzipCodes=[]

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
    else if (postBody.value.length ==0)
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
        if (allzipCodes.includes(postalCode.value))
        {
            submitBtn.click()
            // ShowToastMessage('Valid')
        }
        else
        {
            ShowToastMessage('Please provide Valid Postal Code')
        }

        
    }
    
    

}


function ShowToastMessage(message)
{
    document.getElementById("toastBody").innerHTML = message;
    document.getElementById("toastbtn").click();
}


function ValidateZipCode()
{
    $.ajax({
        type: 'GET',
        url: 'all-zip-codes',
        //data : amcRequest, // data in json format
        success: function (response) {
            //console.log("response", response);
            var zipcodes = response.resp
            for (let zipcode in zipcodes) {
            // console.log("Area : ", zipcodes[zipcode]['zipCode'])
            allzipCodes.push(zipcodes[zipcode]['zipCode'])
            }
            // console.log(allzipCodes)
        },
        error: function (error) {
            //console.log('areaMunicipalityCommunity error')
            console.log(error)
        }
    })

}

ValidateZipCode()