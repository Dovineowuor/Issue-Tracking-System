import Login from './Views/Login/Login';
import { useSelector } from 'react-redux';
import { BrowserRouter as Router ,Routes,Route} from 'react-router-dom';
import Sidebar from './Views/sidenavbar/sidebar';
import Viewbugs from './Views/Pages/viewbugs';
import Createbug from './Views/Bugcreate/bugform';
import Dashboard from './Views/Pages/Dashboard/dashboard';


function App() {
const {auth}=useSelector(state=> state)
return (
<Router>
{!auth.logggined ? <Login/> :
<>
<Sidebar/>
<Routes>
<Route path='/' element={<Dashboard/>} />
<Route path='/viewbugs' element={<Viewbugs/>} />
<Route path='/create' element={<div className='page-container'> <Createbug title="Create Bug"/></div>}/>
</Routes>
</>
}
</Router>
);
}

export default App;