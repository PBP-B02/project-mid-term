$(document).ready(function () {
  $('select').change(function () {
    $(`#total`).remove();
    let totalIncome;
    $.get('/cashflow/json/income', function (incomes) {
      const monthVal = $('select').val();
      const monthlyData = incomes.filter((obj) => {
        let monthNum = new Date(obj.fields.date).getMonth();
        return monthNum == monthVal;
      });
      console.log(monthlyData);
      totalIncome = monthlyData.reduce((total, data) => {
        const amount = data.fields.amount;
        return total + amount;
      }, 0);
      $('.container').append(`<h5 id="total">
          ${totalIncome}
        </h5>`);
    });
  });
});
