# Investigación sobre Sensores y Actuadores en Sistemas Mecatrónicos

---

## 1. Conceptos Básicos

### Explicación con mis propias palabras

- **¿Qué es un sensor?**  
  Un sensor es como el "ojo" o el "oído" de un sistema: Es un dispositivo de entrada que se encarga de detectar o medir una variable física del entorno (como la temperatura, la luz, una distancia o la presión) y la transforma en una señal eléctrica para que el microcontrolador o computadora del sistema pueda entenderla.

- **¿Qué es un actuador?**  
  Un actuador es el "músculo" del sistema: Es un dispositivo de salida que recibe una orden eléctrica procesada por el controlador y la convierte en una acción física o movimiento real en el mundo exterior (como girar una rueda, empujar una palanca, encender un foco o abrir una válvula).

- **Diferencia entre un sensor y un actuador:**  
  La diferencia principal radica en la **dirección de la información y la energía**: el sensor *recibe* estímulos del entorno y envía datos hacia adentro del sistema (entrada), mientras que el actuador *recibe* señales del sistema y realiza una acción hacia afuera en el entorno (salida).

- **Función en un sistema mecatrónico:**  
  Los sensores y actuadores forman el ciclo de control o *retroalimentación* de cualquier sistema mecatrónico: Los sensores permiten que el sistema "sepa" qué está pasando a su alrededor; el cerebro (microcontrolador o PLC) procesa esa información y decide qué hacer; y finalmente, los actuadores ejecutan la acción física necesaria para mantener o cambiar el estado del sistema.

---

### Ejemplo de sistema real: Puerta Automática de Tienda

Un ejemplo muy claro es una **puerta automática de cristal** en un supermercado:

- **Lo que detecta el sensor:** Un sensor de movimiento (infrarrojo o ultrasónico) ubicado sobre la puerta detecta la presencia de una persona acercándose al medir el cambio de movimiento o la reflexión de ondas.

- **La acción del actuador:** El sensor envía una señal a la centralita, la cual activa un **motor eléctrico DC** (el actuador) que gira una banda polea para deslizar las hojas de la puerta y abrir el paso.

---

## 2. Investigación de Sensores

A continuación se muestra la clasificación y características principales de los tipos de sensores más comunes en la industria y la mecatrónica:

| Tipo de Sensor | Variable que mide | Principio de funcionamiento | Ejemplo Comercial | Aplicación Real |
| :---: | :---: | :---: | :---: | :---: |
| **Temperatura** | Temperatura (Calor/Frío) | Variación de la resistencia eléctrica al cambiar la temperatura ambiente (efecto semiconductor o termistor). | LM35 / DHT11 | Control de temperatura en un aire acondicionado o incubadora. |
| **Luz** | Intensidad lumínica | Efecto fotoeléctrico: su resistencia disminuye a mayor cantidad de luz incidente. | LDR (Fotorresistencia) | Encendido automático de las lámparas del alumbrado público. |
| **Proximidad** | Presencia de objeto cercano | Detección de cambios en un campo magnético o electromagnético sin tocar el objeto. | LJ12A3 (Inductivo) | Conteo de latas metálicas en una línea de embotellado. |
| **Distancia** | Distancia física en cm/m | Emite un pulso de sonido agudo y mide el tiempo que tarda en rebotar el eco (tiempo de vuelo). | HC-SR04 (Ultrasónico) | Sensor de reversa en los automóviles para no chocar al estacionarse. |
| **Presión** | Fuerza ejercida por unidad de área | Un diafragma micro-mecánico se deforma con la presión y genera una señal piezoeléctrica. | BMP280 | Estaciones meteorológicas o monitoreo de presión en llantas. |
| **Humedad** | Porcentaje de vapor de agua en el aire | Un material polímero poroso cambia su capacitancia al absorber humedad del ambiente. | DHT22 | Control de clima e irrigación dentro de un invernadero. |
| **Posición** | Ángulo o posición lineal | Divide el voltaje de entrada mediante una pista resistiva variable o cuenta pulsos ópticos. | Potenciómetro / Encoder | Medición del ángulo de giro en las juntas de un brazo robótico. |
| **Velocidad / Movimiento** | RPM o radiación infrarroja térmica | Mide pasos magnéticos por segundo (Efecto Hall) o cambios de calor por movimiento. | Sensor Hall A3144 / PIR | Tacómetro para medir las revoluciones del motor de un coche. |
| **Fuerza o Peso** | Masa o deformación mecánica | Deformación física de un metal medida microscópicamente por galgas extensiométricas. | Célula de carga HX711 | Basculas digitales de supermercado o pesaje industrial de camiones. |

---

## 3. Clasificación de Sensores

Para clasificar correctamente un sensor no basta con saber qué mide, sino analizar **el cómo procesa y entrega su información**:

### A. Sensores Analógicos vs. Digitales

- **Criterio de clasificación:** El tipo de señal de salida que entrega el dispositivo.
- **Analógicos:** Entregan una señal continua en el tiempo que varía proporcionalmente (por ejemplo, un voltaje que cambia gradualmente de 0V a 5V según la temperatura).
- **Digitales:** Entregan valores discretos o binarios (estados de "0" y "1", o paquetes de datos en protocolo I2C/SPI), ideales para conectarse directamente a pines digitales de un microcontrolador.

### B. Sensores de Contacto vs. Sin Contacto

- **Criterio de clasificación:** Si se requiere o no la interacción física directa con el objeto a medir.
- **De contacto:** Necesitan tocar físicamente la pieza o sustancia para tomar la lectura (ejemplo: un interruptor límite de carrera o un termómetro de mercurio).
- **Sin contacto:** Miden variables a distancia mediante campos magnéticos, ondas de luz o ultrasonido, evitando el desgaste mecánico (ejemplo: un sensor infrarrojo).

### C. Sensores Activos vs. Pasivos

- **Criterio de clasificación:** La necesidad de una fuente de alimentación eléctrica externa para operar.
- **Activos:** Requieren energía eléctrica externa para generar una señal o emitir sus propios pulsos (ejemplo: un sensor ultrasónico necesita energía para emitir el sonido).
- **Pasivos:** Generan su propia señal eléctrica directamente a partir del estímulo físico sin requerir alimentación previa (ejemplo: un termopar que genera milivoltios al calentarse o un panel solar).

---

## 4. Investigación de Actuadores

Los actuadores transforman diferentes fuentes de energía en trabajo mecánico útil:

| Actuador | Energía Utilizada | Movimiento Generado | Ventaja Principal | Limitación Principal | Aplicación Real |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Motor DC** | Eléctrica | Rotatorio continuo | Fácil de controlar en velocidad mediante modulación por ancho de pulso (PWM). | Poco torque a bajas velocidades y no sabe en qué ángulo exacto está detenido. | Ruedas de carritos robóticos o ventiladores de computadora. |
| **Servomotor** | Eléctrica | Rotatorio angular preciso (0° a 180°) | Alto torque y control exacto de la posición angular deseada. | Rango de movimiento limitado; no sirve para dar giros continuos e infinitos. | Control de articulaciones en brazos robóticos o timones de drones. |
| **Motor paso a paso** | Eléctrica | Rotatorio por pasos discretos exactos | Control de posición extremadamente preciso sin necesidad de sensores de retroalimentación. | Consume corriente constante incluso al estar detenido y puede perder pasos si se sobrecarga. | Movimiento del cabezal en impresoras 3D y máquinas CNC. |
| **Solenoide** | Eléctrica (Electromagnética) | Lineal corto (empujar/jalar) | Respuesta de activación casi instantánea (On/Off). | Recorrido lineal muy corto (pocos milímetros o centímetros) y fuerza fija. | Cerraduras electrónicas de puertas o pestillos automáticos. |
| **Cilindro Neumático** | Neumática (Aire comprimido) | Lineal continuo de gran recorrido | Movimientos muy rápidos, limpios y seguros para la industria alimentaria. | Dificultad para detener el pistón en posiciones intermedias con precisión. | Empujadores de cajas en líneas de empaque o clasificadoras. |
| **Cilindro Hidráulico** | Hidráulica (Aceite a presión) | Lineal continuo de alta fuerza | Capaz de levantar y mover toneladas de peso con total suavidad. | Instalación compleja, voluminosa, lenta y con riesgo de fugas de aceite. | Brazo principal de una excavadora o maquinaria pesada de construcción. |

---

## 5. Comparación de Actuadores

### A. Motor DC vs. Servomotor

- **Diferencia:** El motor DC gira de forma continua sin control de ángulo exacto, mientras que el servomotor incluye un sistema interno de retroalimentación que le permite posicionarse y quedarse firme en un ángulo específico (ej. 45° o 90°).
- **¿Cuál elegir y por qué?:** Elegiría un **Servomotor** para controlar el timón de un barco a escala, porque necesito mantener la pala fija en un ángulo específico para girar la embarcación con precisión, cosa que un motor DC continuo no podría hacer.

### B. Servomotor vs. Motor Paso a Paso

- **Diferencia:** El servomotor suele estar limitado a giros de 180° o 360° con una posición referenciada por potenciómetro interno, mientras que el motor paso a paso puede dar giros infinitos divididos en cientos de micro-pasos exactos.
- **¿Cuál elegir y por qué?:** Elegiría un **Motor paso a paso** para la banda de una impresora 3D, ya que necesita girar miles de vueltas en ambas direcciones manteniendo una precisión micrométrica sin perder la referencia de su ubicación.

### C. Actuador Neumático vs. Actuador Hidráulico

- **Diferencia:** El neumático utiliza aire comprimido (rápido, limpio, fuerza moderada), mientras que el hidráulico utiliza aceite incompresible a alta presión (movimiento más lento pero fuerza extrema).
- **¿Cuál elegir y por qué?:** Elegiría un **Actuador neumático** para una línea de empaque de medicamentos o alimentos, ya que si ocurre un fallo o fuga, el aire comprimido no contamina el producto, a diferencia del aceite hidráulico.

---

## 6. Sensores y Actuadores en un Sistema Real

### Sistema Seleccionado: Sistema de Riego Automático Inteligente

Este sistema se encarga de monitorear la tierra de un cultivo y regar las plantas solo cuando sea necesario.

- **Sensores utilizados:**

  1. **Sensor de humedad de suelo (YL-69):** Mide la cantidad de agua presente en la tierra.
  2. **Sensor de temperatura y humedad ambiental (DHT11):** Revisa el clima ambiente para evitar regar a horas de calor extremo.

- **Actuadores utilizados:**

  1. **Electroválvula de agua (Solenoide):** Abre o cierra el paso del agua de la tubería principal.
  2. **Bomba de agua de 12V (Motor DC acoplado):** Impulsa el agua desde el depósito hacia los aspersores cuando se activa.

---

### Diagrama de Relación del Sistema

```text
 [ Sensor Humedad Suelo ] ----\
                               +---> [ Controlador / Arduino ] ---> [ Relé / Driver ] ---> [ Bomba de Agua (Motor DC) ]
 [ Sensor Clima DHT11 ] ------/                                                      ----> [ Electroválvula (Solenoide) ]
```

## 7. Selección de Componentes para Situaciones Prácticas

1. **Detectar si una persona se encuentra frente a una puerta automática:**

   - **Componente:** Sensor PIR (Infrarrojo Pasivo) o Sensor Ultrasónico.
   - **Razón:** Detecta el calor corporal en movimiento o la variación de distancia sin importar las condiciones de luz.

2. **Medir la temperatura dentro de un salón:**

   - **Componente:** Sensor analógico LM35 o digital DHT11.
   - **Razón:** Tienen un rango de medición perfecto para temperaturas ambiente humanas (0°C a 50°C) con muy buen margen de precisión.

3. **Detectar el nivel de agua de un depósito:**

   - **Componente:** Sensor de distancia Ultrasónico (HC-SR04) colocado en la tapa superior.
   - **Razón:** Permite medir la distancia restante hasta la superficie del agua sin estar sumergido, evitando la corrosión del sensor.

4. **Mover una rueda de un robot móvil:**

   - **Componente:** Motor de corriente directa (DC) con caja reductora.
   - **Razón:** Proporciona un giro continuo eficiente con el torque necesario para vencer la fricción del suelo y desplazar el robot.

5. **Controlar con precisión el ángulo de una pequeña articulación robótica:**

   - **Componente:** Servomotor SG90 o MG996R.
   - **Razón:** Permite ajustar el ángulo de la junta con precisión entre 0° y 180° mediante una simple señal de control PWM.

6. **Empujar una pieza en una línea de producción:**

   - **Componente:** Cilindro neumático de doble efecto.
   - **Razón:** Realiza un movimiento de avance y retroceso lineal rápido, limpio y muy repetitivo.

7. **Medir la distancia entre un robot y una pared:**

   - **Componente:** Sensor Ultrasónico HC-SR04.
   - **Razón:** Ofrece lecturas rápidas de distancia entre 2 cm y 400 cm mediante el rebote de sonido, ideal para evitar colisiones.

8. **Detectar si una habitación está iluminada:**

   - **Componente:** Fotorresistencia LDR.
   - **Razón:** Su resistencia cambia drásticamente en presencia de luz visible, lo que permite implementar un circuito de detección muy sencillo y económico.

---

## Reflexión Final

El medir una variable física implica el recopilar información del estado actual del entorno mediante un sensor sin alterarlo, mientras que realizar una acción física significa usar un actuador para modificar activamente las condiciones de ese entorno. 
Esta diferencia refleja la esencia de la mecatrónica: la interacción constante entre la percepción y la respuesta.

Un sistema mecatrónico necesita obligatoriamente tanto de sensores como de actuadores porque forman un ciclo cerrado de control; los sensores funcionan como los sentidos que permiten interpretar el mundo, y los actuadores son las herramientas que permiten intervenir en él. 
Si un sistema solo tuviera actuadores, trabajaría "a ciegas" sin saber si logró su objetivo; y si solo tuviera sensores, sabría exactamente qué ocurre pero sería totalmente incapaz de reaccionar.

Entre todos los dispositivos analizados, el motor paso a paso me pareció el más interesante. La capacidad de dividir una rotación completa en pasos microscópicos y exactos mediante pulsos electromagnéticos "sin necesidad de un sensor de posición de retorno" demuestra un diseño de ingeniería sumamente ingenioso que hace posible tecnologías cotidianas clave como las impresoras 3D.

---

## Referencias

1. Ogata, K. (2010). *Ingeniería de Control Moderna* (5ta ed.). Pearson Educación.
2. Bolton, W. (2013). *Mecatrónica: Sistemas de control electrónico en ingeniería mecánica y eléctrica* (5ta ed.). Alfaomega.
3. Texas Instruments. (2015). *LM35 Precision Centigrade Temperature Sensors (Datasheet)*. https://www.ti.com/lit/ds/symlink/lm35.pdf
4. SparkFun Electronics. (2020). *Beginner's Guide to Sensors and Actuators*. SparkFun Learn. https://learn.sparkfun.com/
5. Festo Didactic. (2019). *Fundamentos de Neumática e Hidráulica Industrial*. Festo SE & Co. KG.