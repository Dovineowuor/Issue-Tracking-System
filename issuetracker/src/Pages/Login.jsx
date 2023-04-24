import React, { useEffect, useState } from 'react'

const Login = () => {
    const [ year, setYear ] = useState()

    useEffect(()=>{
        const getYear = () =>{
            setYear(new Date().getFullYear())
        };
        getYear();
    },[])
    
    return (
        <div className="font-sans min-h-screen antialiased bg-gray-900 pt-24 pb-5">
            <div className="flex flex-col justify-center  sm:w-96 sm:m-auto mx-5 mb-5 space-y-8">
                <h1 className="font-bold text-center text-4xl text-yellow-500">Issue<span className="text-blue-500">Tracker</span></h1>
                <form action="#">
                    <div className="flex flex-col bg-white p-10 rounded-lg shadow space-y-6">
                        <h1 className="font-bold text-xl text-center">Log in to your account</h1>

                        <div className="flex flex-col space-y-1">
                            <input type="email" name="email" id="username" className="border-2 rounded px-3 py-2 w-full focus:outline-none focus:border-blue-400 focus:shadow" placeholder="Email" />
                        </div>

                        <div className="flex flex-col space-y-1">
                            <input type="password" name="password" id="password" className="border-2 rounded px-3 py-2 w-full focus:outline-none focus:border-blue-400 focus:shadow" placeholder="Password" />
                        </div>

                        <div className="flex gap-1">
                            <input type="checkbox" name="remember" id="remember"  className="inline-block align-middle" />
                            <label className="inline-block align-middle">Remember me</label>
                        </div>

                        <div className="flex flex-col-reverse sm:flex-row sm:justify-between items-center">
                            <a href="#!" className="inline-block text-blue-500 hover:text-blue-800 hover:underline">Forgot your password?</a>
                            <button type="submit" className="bg-blue-500 text-white font-bold px-5 py-2 rounded focus:outline-none shadow hover:bg-blue-700 transition-colors">Log In</button>
                        </div>
                    </div>
                </form>
                <div className="flex justify-center text-gray-500 text-sm">
                    <p>&copy;{year}. All right reserved.</p>
                </div>
            </div>
        </div>
    )
}

export default Login