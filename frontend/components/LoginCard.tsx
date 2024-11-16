import * as React from "react"
import "../app/globals.css"
import { Button } from "@/components/ui/button"
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"

export function LoginCard() {
    return (
        <Card className="w-[350px]">
            <CardHeader>
                <CardTitle>Simplify your inbox</CardTitle>
                <CardDescription>Summarize your emails into one readable email.</CardDescription>
            </CardHeader>
            <CardContent>
                {/* Removed form and input elements */}
            </CardContent>
            <CardFooter className="flex justify-center">
                {/* Only one button now */}
                <Button>Get Started with your Gmail</Button>
            </CardFooter>
        </Card>
    );
}
