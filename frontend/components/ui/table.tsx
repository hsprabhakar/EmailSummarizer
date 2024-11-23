export default function Table() {
  return (
    <div className="overflow-x-auto">
    <table className="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
        <thead className="ltr:text-left rtl:text-right">
        <tr>
            <th className="whitespace-nowrap px-3 py-2 font-medium text-gray-900">ID</th>
            <th className="whitespace-nowrap px-3 py-2 font-medium text-gray-900">Title</th>
            <th className="whitespace-nowrap px-3 py-2 font-medium text-gray-900">Body</th>
        </tr>
        </thead>

        <tbody className="divide-y divide-gray-200">
        <tr>
            <td className="whitespace-nowrap px-3 py-2 font-medium text-gray-900">1</td>
            <td className="whitespace-nowrap px-3 py-2 text-gray-700">Amazon Inc</td>
            <td className="whitespace-nowrap px-3 py-2 text-gray-700">...</td>
        </tr>

        <tr>
            <td className="whitespace-nowrap px-3 py-2 font-medium text-gray-900">2</td>
            <td className="whitespace-nowrap px-3 py-2 text-gray-700">Pizza Hut</td>
            <td className="whitespace-nowrap px-3 py-2 text-gray-700">...</td>
        </tr>

        <tr>
            <td className="whitespace-nowrap px-3 py-2 font-medium text-gray-900">3</td>
            <td className="whitespace-nowrap px-3 py-2 text-gray-700">CRA</td>
            <td className="whitespace-nowrap px-3 py-2 text-gray-700">...</td>
        </tr>
        </tbody>
    </table>
    </div>

  )
}