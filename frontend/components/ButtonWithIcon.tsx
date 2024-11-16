import { Button } from "@/components/ui/button";
import "../app/globals.css";

interface ButtonWithIconProps {
    icon: React.ReactNode;
    label: string;
    onClick: () => void;
}

export function ButtonWithIcon({ icon, label, onClick }: ButtonWithIconProps) {
    return (
        <Button 
        className="flex items-center gap-2 border border-gray-300 px-4 py-2 rounded-md shadow-sm hover:bg-gray-100"
        onClick={onClick}>
        {icon}
        {label}
        </Button>
    );
}
