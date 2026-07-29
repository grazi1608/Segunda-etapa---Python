







PS H:\python\Aula15-API> ^C
PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Car","autor":"Eu","ano":2021}'


ano          : 2021
autor        : Eu
data_criacao : 2026-07-29 09:09:49.172889
id           : 4
titulo       : Car



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":irmaos hawthornes","autor":"jennifer","ano":2024}'
Invoke-RestMethod : 
400 Bad Request
Bad Request
Failed to decode JSON object: Expecting value: line 1 column 11 (char 10)
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car2","autor":"eu","ano":2023}'
>>


ano          : 2023
autor        : eu
data_criacao : 2026-07-29 09:15:29.754763
id           : 5
titulo       : car2



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"jogos de herança","autor":"eu","ano":2024}'
>>
Invoke-RestMethod : 
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe7 in position 25: invalid continuation byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car4","autor":"eu","ano":2025}'
>>


ano          : 2025
autor        : eu
data_criacao : 2026-07-29 09:17:46.490419
id           : 6
titulo       : car4



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car5O","autor":"eu","ano":2O23}'
Invoke-RestMethod : 
400 Bad Request
Bad Request
Failed to decode JSON object: Expecting &#39;,&#39; delimiter: line 1 column 39 (char 38)
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car5","autor":"eu","ano":2023}'
>>


ano          : 2023
autor        : eu
data_criacao : 2026-07-29 09:19:46.760437
id           : 7
titulo       : car5



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car6","autor":"eu","ano":2023}'


ano          : 2023
autor        : eu
data_criacao : 2026-07-29 09:20:28.399919
id           : 8
titulo       : car6



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car7","autor":"eu","ano":2027}'
>>


ano          : 2027
autor        : eu
data_criacao : 2026-07-29 09:21:06.085670
id           : 9
titulo       : car7



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car8","autor":"eu","ano":2024}'
>>


ano          : 2024
autor        : eu
data_criacao : 2026-07-29 09:21:41.447706
id           : 10
titulo       : car8



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car9","autor":"eu","ano":2020}'
>>


ano          : 2020
autor        : eu
data_criacao : 2026-07-29 09:22:13.042053
id           : 11
titulo       : car9



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car10","autor":"eu","ano":2021}'
>>


ano          : 2021
autor        : eu
data_criacao : 2026-07-29 09:22:52.039939
id           : 12
titulo       : car10



PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"NOME DO LIVRO","autor":"","ano":2020}'
>>
Invoke-RestMethod : {
  "erro": "T\u00edtulo e autor n\u00e3o podem ser vazios"
}
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS H:\python\Aula15-API> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"car11","autor":"eu","ano":2020}'
>>


ano          : 2020
autor        : eu
data_criacao : 2026-07-29 09:24:01.084927
id           : 13
titulo       : car11



PS H:\python\Aula15-API> -Method PUT `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Cotemig","autor":"3A1","ano":2026}'
>>
-Method : O termo '-Method' não é reconhecido como nome de cmdlet, função, arquivo de script ou programa operável. Verifique a grafia do nome ou, se um caminho tiver sido incluído, veja se o caminho está 
correto e tente novamente.
No linha:1 caractere:1
+ -Method PUT `
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (-Method:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS H:\python\Aula15-API> -Method PUT `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"janaina","autor":"3b1","ano":2026}'
>>
-Method : O termo '-Method' não é reconhecido como nome de cmdlet, função, arquivo de script ou programa operável. Verifique a grafia do nome ou, se um caminho tiver sido incluído, veja se o caminho está 
correto e tente novamente.
No linha:1 caractere:1
+ -Method PUT `
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (-Method:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS H:\python\Aula15-API> ^C
PS H:\python\Aula15-API>  Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 `
>> >>   -Method PUT `
>> >>   -ContentType "application/json" `
>>  -Body '{"titulo":"janaina","autor":"3b1","ano":2026}'
>>
No linha:3 caractere:1
+ >>   -ContentType "application/json" `
+ ~~~~~~~~~~~~~~~~~
O fluxo de saída deste comando já foi redirecionado.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : StreamAlreadyRedirected