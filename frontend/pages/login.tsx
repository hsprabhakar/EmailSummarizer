import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import {DetailsAccordion} from "@/components/DetailsAccordion"
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion"
import { GoogleLoginButton } from "@/components/EmailButton"
import "../app/globals.css"
export default function Login() {
    return (
        <div className="flex h-screen">
            {/* Left side - Content */}
            <div className="flex-1 bg-gray-100 flex items-center justify-center">
            <div className="text-center">
                <h1 className="text-4xl font-bold mb-4">Simplify your inbox</h1>
                <p className="text-lg text-gray-600">Summarize your emails into one readable email, everyday</p>
                <div className="mt-10">
                    <DetailsAccordion />
                </div>
            </div>
            </div>
    
            {/* Right side - Signup Card */}
            <div className="flex-1 bg-white flex items-center justify-center">
            <Card className="w-[400px] shadow-lg p-6">
                <CardHeader>
                <CardTitle>Authenticate your Account</CardTitle>
                <CardDescription>Sign up in just a few easy steps.</CardDescription>
                </CardHeader>
                <CardContent>
                </CardContent>
                <CardFooter className="flex flex-col space-y-2">
                <GoogleLoginButton />    
                </CardFooter>
            </Card>
            </div>
        </div>
        );
    }
    