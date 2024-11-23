"use client";

import { ButtonWithIcon } from "@/components/ButtonWithIcon";
import { useRouter } from "next/navigation";


export function GoogleLoginButton() {
    const router = useRouter(); // Initialize the router

    const handleGoogleLogin = async () => {
        try {
            const response = await fetch("http://localhost:8000/api/auth/google", {
                method: "GET",
                credentials: "include"
            });

            if (response.ok) {
                const {redirect_url} = await response.json();
                window.location.href = "/home";
            } else {
                throw new Error("Failed to login with Google");
            }
            
        } catch (error) {
            console.error("Failed to login with Google", error);
        }
    }


    return (
        <ButtonWithIcon
        icon={<img src="google-icon.svg" alt="Google Icon" className="w-5 h-5" />}
        label="Google"
        onClick={handleGoogleLogin}
        />
    );
}
