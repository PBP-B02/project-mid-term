$(document).ready(function () {
  $('form').submit(function (e) {
    e.preventDefault();
    var budgetVal = $('#id_budget_type').val();

    // konversi ke dalam format mata uang rupiah
    const rupiah = new Intl.NumberFormat('id-ID', {
      style: 'currency',
      currency: 'IDR',
      maximumFractionDigits: 0,
    });

    if (budgetVal == 'income') {
      let totalIncome;
      let monthlyData;

      // menghitung total amount income
      $.get('/cashflow/json/income', function (incomes) {
        const monthVal = $('#id_month_field').val();
        monthlyData = incomes.filter((obj) => {
          let monthNum = new Date(obj.fields.date).getMonth();
          return monthNum == monthVal;
        });

        totalIncome = monthlyData.reduce((total, data) => {
          const amount = data.fields.amount;
          return total + amount;
        }, 0);
        $(`#totalAmount`).empty();
        $('#totalAmount').append(`<h5>Total ${budgetVal} : ${rupiah.format(totalIncome)}</h5>`);

        // mengirimkan data history baru ke views
        $.post(
          '/history/add-history/',
          {
            budget_type: budgetVal,
            month_field: $('#id_month_field').val(),
            amount: totalIncome,
          },
          function (new_history) {
            console.log(new_history);
          }
        );

        // menampilkan data income sesuai bulan
        $(`.history`).empty();
        for (i = 0; i < monthlyData.length; i++) {
          $('.history').append(`<tr id="${monthlyData[i].pk}_income">
                      <th scope="row">${i + 1}</th>
                      <td>${monthlyData[i].fields.date}</td>
                      <td>${monthlyData[i].fields.name}</td>
                      <td>${monthlyData[i].fields.income_type}</td>
                      <td>${rupiah.format(monthlyData[i].fields.amount)}</td>
                      </tr>`);
        }
      });
    } else if (budgetVal == 'spending') {
      let totalSpending;
      let monthlyData;

      // menghitung total amount spending
      $.get('/cashflow/json/spending', function (spending) {
        const monthVal = $('#id_month_field').val();
        monthlyData = spending.filter((obj) => {
          let monthNum = new Date(obj.fields.date).getMonth();
          return monthNum == monthVal;
        });
        totalSpending = monthlyData.reduce((total, data) => {
          const amount = data.fields.amount;
          return total + amount;
        }, 0);
        $(`#totalAmount`).empty();
        $('#totalAmount').append(`<h5>Total ${budgetVal} : ${rupiah.format(totalSpending)}</h5>`);

        // mengirimkan data history baru ke views
        $.post(
          '/history/add-history/',
          {
            budget_type: budgetVal,
            month_field: $('#id_month_field').val(),
            amount: totalSpending,
          },
          function (new_history) {
            console.log(new_history);
          }
        );

        // menampilkan data spending sesuai bulan
        $(`.history`).empty();
        for (i = 0; i < monthlyData.length; i++) {
          $('.history').append(`<tr id="${monthlyData[i].pk}_spending">
                      <th scope="row">${i + 1}</th>
                      <td>${monthlyData[i].fields.date}</td>
                      <td>${monthlyData[i].fields.name}</td>
                      <td>${monthlyData[i].fields.spending_type}</td>
                      <td>${rupiah.format(monthlyData[i].fields.amount)}</td>
                      </tr>`);
        }
      });
    }
  });
});
