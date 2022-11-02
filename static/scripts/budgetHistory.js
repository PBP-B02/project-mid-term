$(document).ready(function () {
  $('form').submit(function (e) {
    e.preventDefault();
    var budgetVal = $('#id_budget_type').val();
    if (budgetVal == 'income') {
      let totalIncome;
      $.get('/cashflow/json/income', function (incomes) {
        const monthVal = $('#id_month_field').val();
        const monthlyData = incomes.filter((obj) => {
          let monthNum = new Date(obj.fields.date).getMonth();
          return monthNum == monthVal;
        });
        totalIncome = monthlyData.reduce((total, data) => {
          const amount = data.fields.amount;
          return total + amount;
        }, 0);
        console.log(totalIncome);
        console.log(budgetVal);
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
      });
    } else if (budgetVal == 'spending') {
      let totalSpending;
      $.get('/cashflow/json/spending', function (spending) {
        const monthVal = $('#id_month_field').val();
        const monthlyData = spending.filter((obj) => {
          let monthNum = new Date(obj.fields.date).getMonth();
          return monthNum == monthVal;
        });
        totalSpending = monthlyData.reduce((total, data) => {
          const amount = data.fields.amount;
          return total + amount;
        }, 0);
        console.log(totalSpending);
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
      });
    }

    // $.get('/history/json/', function (history) {
    //   console.log(history);
    // });
  });
  // $('#id_budget_type_0').click(function () {
  //   $("input[type='radio'][id='id_budget_type_0']:checked").val('income');
  // });
  // $('#id_budget_type_1').click(function () {
  //   $("input[type='radio'][id='id_budget_type_0']:checked").val('income');
  // });
});
