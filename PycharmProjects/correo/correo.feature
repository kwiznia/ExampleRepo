Feature: Correo Gmail

Scenario: Abrir el correo satisfactoriamente
    Given open the main page
    When write my username
    And write my password
    And press the sign in button <button>
    Then check the write new message button <button>


Examples:
| 'button' |
| 'button' |

