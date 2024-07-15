function calculateEMI() {
    var principal = parseFloat(document.getElementById('principal').value);
    var rate = parseFloat(document.getElementById('rate').value);
    var tenure = parseFloat(document.getElementById('tenure').value);

    if (isNaN(principal) || isNaN(rate) || isNaN(tenure) || principal <= 0 || rate <= 0 || tenure <= 0) {
        alert("Please fill all fields with valid values");
        return;
    }

    var monthlyRate = (rate / 12) / 100;
    var numberOfMonths = tenure * 12;

    var emi = (principal * monthlyRate * Math.pow((1 + monthlyRate), numberOfMonths)) / (Math.pow((1 + monthlyRate), numberOfMonths) - 1);
    emi = emi.toFixed(2);

    var totalPayment = emi * numberOfMonths;
    var totalInterest = totalPayment - principal;

    document.getElementById('result').innerHTML = `
        Monthly EMI: RS ${emi} <br>
        Total Interest Payable: RS ${totalInterest.toFixed(2)} <br>
        Total Payment (Principal + Interest): RS ${totalPayment.toFixed(2)}
    `;

    displayAmortizationSchedule(principal, rate, tenure, emi);
}

function displayAmortizationSchedule(principal, rate, tenure, emi) {
    var monthlyRate = (rate / 12) / 100;
    var numberOfMonths = tenure * 12;
    var remainingPrincipal = principal;
    var yearlyAmortization = [];

    for (var year = 1; year <= tenure; year++) {
        var interestPaidYear = 0;
        var principalPaidYear = 0;

        for (var month = 1; month <= 12; month++) {
            var interestPaidMonth = remainingPrincipal * monthlyRate;
            var principalPaidMonth = emi - interestPaidMonth;

            interestPaidYear += interestPaidMonth;
            principalPaidYear += principalPaidMonth;

            remainingPrincipal -= principalPaidMonth;
        }

        yearlyAmortization.push({
            year: year,
            interestPaid: interestPaidYear.toFixed(2),
            principalPaid: principalPaidYear.toFixed(2),
            remainingPrincipal: remainingPrincipal.toFixed(2)
        });
    }

    var amortizationTable = '<table border="1" cellpadding="5"><tr><th>Year</th><th>Interest Paid (RS)</th><th>Principal Paid (RS)</th><th>Remaining Principal (RS)</th></tr>';

    yearlyAmortization.forEach(function (yearData) {
        amortizationTable += `<tr>
            <td>${yearData.year}</td>
            <td>RS ${yearData.interestPaid}</td>
            <td>RS ${yearData.principalPaid}</td>
            <td>RS ${Math.abs(yearData.remainingPrincipal)}</td>
        </tr>`;
    });

    amortizationTable += '</table>';

    document.getElementById('amortization').innerHTML = amortizationTable;
}
