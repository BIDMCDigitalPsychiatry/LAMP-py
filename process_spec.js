import fs from 'node:fs'


const fileName = process.argv[2]

console.log("Processing: ", fileName)

const spec = JSON.parse(fs.readFileSync(fileName, "utf-8"))

const newPaths = {}

for (let [pathName, path] of Object.entries(spec.paths)) {
    let newPath = {}
    let newPathName = pathName
    for (let [method, operation] of Object.entries(path)) {
        // Do not generate client functions for endpoints marked with "x-internal"
        if (!operation["x-internal"]) {
            newPath[method] = operation
        }

        const pythonSettings = operation["x-python-settings"]
        if (pythonSettings) {
            // Set the name of the method to be generated for the sdk
            if (pythonSettings.name) {
                operation.operationId = pythonSettings.name
            }

            // Remove request body type checking. 
            // Useful when the request body can have more than one type which is not supported by generator version 5.3.1
            if (pythonSettings.anyJsonRequestBody) {             
                operation.requestBody.content = {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "additionalProperties": true
                        }
                    }
                }
            }

            // Replace path parameters with their defined defaults
            if (pythonSettings.pathParameterDefaults) {
                let currentPathName = pathName
                for (let [parameterName, defaultValue] of Object.entries(pythonSettings.pathParameterDefaults)) {
                    console.log(`${currentPathName} => `, currentPathName.replace(`{${parameterName}}`, defaultValue))
                    currentPathName = currentPathName.replace(`{${parameterName}}`, defaultValue)
                    operation.parameters = operation.parameters.filter((param) => !(param.name === parameterName && param.in === "path"))
                }
                newPathName = currentPathName
            }
        }
    }

    if (Object.keys(newPath).length) {
        newPaths[newPathName] = newPath
    }
}

spec.paths = newPaths
console.log(spec)

fs.writeFileSync('./processed_spec.json', JSON.stringify(spec));