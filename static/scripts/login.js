const usernameField = document.querySelector("#username");
const submitBtn = document.querySelector(".btn");

usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    if (usernameVal.length > 0) {
      fetch("/auth/validate_login_username/", {
        body: JSON.stringify({ username: usernameVal }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.username_valid) {
            submitBtn.removeAttribute("disabled");
            usernameField.classList.remove("is-invalid");
            usernameField.classList.add("is-valid");
          } else {
            submitBtn.disabled = true;
            usernameField.classList.remove("is-valid");
            usernameField.classList.add("is-invalid");
          }
        });
    } else {
        fetch("/auth/validate_username/", {
            body: JSON.stringify({ username: usernameVal }),
            method: "POST",
          })
          .then((res) => res.json())
          .then((data) => {
            console.log("data", data);
            usernameField.classList.remove("is-invalid");
            usernameField.classList.remove("is-valid");
          });
        }
    });