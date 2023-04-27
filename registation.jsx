var MyClass = React.createClass({
  render: function() {
    return (
      <div>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
        <meta name="description" content="Bootstrap Admin App + jQuery" />
        <meta name="keywords" content="app, responsive, jquery, bootstrap, dashboard, admin" />
        <title>ISSUE TRACKING SYSTEM</title>
        {/* =============== VENDOR STYLES ===============*/}
        {/* FONT AWESOME*/}
        <link rel="stylesheet" href="../vendor/fontawesome/css/font-awesome.min.css" />
        {/* SIMPLE LINE ICONS*/}
        <link rel="stylesheet" href="../vendor/simple-line-icons/css/simple-line-icons.css" />
        {/* =============== BOOTSTRAP STYLES ===============*/}
        <link rel="stylesheet" href="css/bootstrap.css" id="bscss" />
        {/* =============== APP STYLES ===============*/}
        <link rel="stylesheet" href="css/app.css" id="maincss" />
        <div className="wrapper">
          <div className="block-center mt-xl wd-xl">
            {/* START panel*/}
            <div className="panel panel-dark panel-flat">
              <div className="panel-heading text-center">
                <a href="#">
                  <img src="img/logo.png" alt="Image" className="block-center img-rounded" />
                </a>
              </div>
              <div className="panel-body">
                <p className="text-center pv">SIGNUP TO TRACK ISSUE.</p>
                <form role="form" data-parsley-validate noValidate className="mb-lg">
                  <div className="form-group has-feedback">
                    <label htmlFor="signupInputEmail1" className="text-muted">Email address</label>
                    <input id="signupInputEmail1" type="email" placeholder="Enter email" autoComplete="off" required className="form-control" />
                    <span className="fa fa-envelope form-control-feedback text-muted" />
                  </div>
                  <div className="form-group has-feedback">
                    <label htmlFor="signupInputPassword1" className="text-muted">Password</label>
                    <input id="signupInputPassword1" type="password" placeholder="Password" autoComplete="off" required className="form-control" />
                    <span className="fa fa-lock form-control-feedback text-muted" />
                  </div>
                  <div className="form-group has-feedback">
                    <label htmlFor="signupInputRePassword1" className="text-muted">Retype Password</label>
                    <input id="signupInputRePassword1" type="password" placeholder="Retype Password" autoComplete="off" required data-parsley-equalto="#signupInputPassword1" className="form-control" />
                    <span className="fa fa-lock form-control-feedback text-muted" />
                  </div>
                  <div className="clearfix">
                    <div className="checkbox c-checkbox pull-left mt0">
                      <label>
                        <input type="checkbox" defaultValue required name="agreed" />
                        <span className="fa fa-check" />I agree with the <a href="#">terms</a>
                      </label>
                    </div>
                  </div>
                  <button type="submit" className="btn btn-block btn-primary mt-lg">Create account</button>
                </form>
                <p className="pt-lg text-center">Have an account?</p><a href="login.html" className="btn btn-block btn-default">Signup</a>
              </div>
            </div>
            {/* END panel*/}
            <div className="p-lg text-center">
              <span>©</span>
              <span>2016</span>
              <span>-</span>
              <span>ISSUE TRACKING SYSTEM</span>
              <br />
              <span>ALX PROJECT</span>
            </div>
          </div>
        </div>
        {/* =============== VENDOR SCRIPTS ===============*/}
        {/* MODERNIZR*/}
        {/* JQUERY*/}
        {/* BOOTSTRAP*/}
        {/* STORAGE API*/}
        {/* PARSLEY*/}
        {/* =============== APP SCRIPTS ===============*/}
      </div>
    );
  }
});
