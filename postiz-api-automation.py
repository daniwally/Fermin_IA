#!/usr/bin/env python3
"""
Postiz API Automation for The Agents
Uploads images and schedules 5 Instagram posts automatically
"""

import requests
import json
from datetime import datetime
import os

class PostizAutomation:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.postiz.com/public/v1"
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json"
        }
    
    def upload_image(self, image_path):
        """Upload image to Postiz and return image object"""
        upload_url = f"{self.base_url}/upload"
        
        with open(image_path, 'rb') as f:
            files = {'file': f}
            headers = {"Authorization": self.api_key}  # No Content-Type for multipart
            
            response = requests.post(upload_url, headers=headers, files=files)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to upload {image_path}: {response.text}")
                return None
    
    def get_integrations(self):
        """Get list of connected social media accounts"""
        response = requests.get(f"{self.base_url}/integrations", headers=self.headers)
        return response.json() if response.status_code == 200 else None
    
    def create_scheduled_post(self, integration_id, content, image_obj, schedule_date):
        """Create a scheduled Instagram post"""
        
        post_data = {
            "type": "schedule",
            "date": schedule_date,
            "shortLink": False,
            "tags": [],
            "posts": [{
                "integration": {"id": integration_id},
                "value": [{
                    "content": content,
                    "image": [image_obj] if image_obj else []
                }],
                "settings": {
                    "__type": "instagram",
                    "post_type": "post"
                }
            }]
        }
        
        response = requests.post(
            f"{self.base_url}/posts", 
            headers=self.headers, 
            data=json.dumps(post_data)
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to create post: {response.text}")
            return None

def main():
    # Configuration
    API_KEY = "YOUR_POSTIZ_API_KEY"  # Replace with actual API key
    
    # Post data
    posts = [
        {
            "image": "2026-03-08-theagents-post1-5tareas.png",
            "date": "2026-03-10T13:00:00.000Z",  # 10am Argentina = 1pm UTC
            "content": """🌙 Mientras vos dormís, tu agente IA trabaja.

5 tareas que nunca más vas a tener que hacer:

💌 FOLLOW-UP AUTOMÁTICO
→ Responde leads en menos de 30 segundos
→ Nurturing personalizado según comportamiento
→ Nunca más un prospect "frío" por falta de seguimiento

📊 LEAD SCORING INTELIGENTE  
→ Analiza 200+ data points por lead
→ Prioriza automáticamente tu pipeline
→ Te dice exactamente cuándo contactar

📅 CALENDAR MANAGEMENT
→ Agenda reuniones según tu disponibilidad
→ Confirma, reagenda y optimiza tu tiempo
→ Prep automático antes de cada meeting

📈 REPORTES EN TIEMPO REAL
→ Métricas actualizadas 24/7
→ Alertas cuando algo requiere atención  
→ Insights para tomar mejores decisiones

🔍 COMPETITOR TRACKING
→ Monitorea precios, productos, estrategias
→ Alertas cuando cambia el mercado
→ Te mantiene siempre un paso adelante

¿Tu competencia ya duerme tranquila sabiendo que su agente trabaja?

👇 Comentá "DEMO" y te mostramos cómo funciona

#AgentesIA #Automatización #ProductividadEmpresarial #TheAgents #IAArgentina"""
        },
        {
            "image": "2026-03-08-theagents-post2-costo.png",
            "date": "2026-03-12T13:00:00.000Z",
            "content": """💸 El costo oculto que nadie calcula

EMPRESA SIN AGENTE IA:
❌ 47% de leads sin follow-up (fuente: HubSpot)
❌ 15 horas/semana en tareas repetitivas  
❌ Respuesta promedio: 24 horas
❌ Conversión: 2.3%
❌ Errores humanos: 8% de los procesos

EMPRESA CON AGENTE IA:
✅ 100% de leads con seguimiento automático
✅ 15 horas/semana libres para estrategia
✅ Respuesta promedio: 30 segundos  
✅ Conversión: 8.7% 
✅ Errores: 0.02%

💰 ROI REAL de no actuar:
• Lead perdido promedio: $2,500
• 47% sin seguimiento = $82,250/mes perdidos
• Costo oportunidad anual: $987,000

🔥 Costo de nuestro agente: $6,000/mes
💵 Retorno promedio: $25,000/mes adicional

La pregunta no es si podés permitirte un agente IA.
La pregunta es: ¿podés permitirte NO tenerlo?

📊 ¿Calculamos tu ROI específico?
Link en bio para assessment gratuito.

#ROI #AgentesIA #CostosOcultos #TheAgents #Automatización"""
        },
        {
            "image": "2026-03-08-theagents-post3-vs-empleado.png", 
            "date": "2026-03-14T13:00:00.000Z",
            "content": """🥊 ROUND 1: Agente IA vs Empleado Tradicional

👤 EMPLEADO TRADICIONAL:
⏰ Horario: 8 horas/día  
💰 Costo anual: $60,000 + beneficios
🏖️ Vacaciones: 20 días/año
😴 Sick days: 5-8 días/año
🧠 Capacidad: 1x velocidad humana
📚 Training: 3-6 meses onboarding
⚡ Multitasking: 3-4 tareas máximo

🤖 AGENTE IA:
⏰ Horario: 24/7/365 sin parar
💰 Costo anual: $72,000 total
🏖️ Vacaciones: 0 días (obvio)  
😴 Downtime: 0.01% (mantenimiento)
🧠 Capacidad: 1000x velocidad humana
📚 Training: Deploy en 48 horas
⚡ Multitasking: Infinitas tareas simultáneas

🏆 WINNER: ¿Necesitás que te lo digamos?

No es reemplazar personas.
Es liberar talento humano para cosas que SÍ importan:
• Estrategia
• Creatividad  
• Relaciones
• Innovación

¿Tu equipo está listo para this level up?

💬 Comentá "LEVEL" para ver cómo transformamos equipos

#ProductividadIA #TransformaciónDigital #TheAgents #FuturoDelTrabajo"""
        },
        {
            "image": "2026-03-08-theagents-post4-3errores.png",
            "date": "2026-03-17T13:00:00.000Z", 
            "content": """⚠️ 3 errores que arruinan tu implementación de IA

ERROR #1: "Compramos IA y ya"
❌ Implementar herramientas sin estrategia
❌ No definir objetivos claros
❌ Esperar magia automática

✅ LO CORRECTO:
→ Audit completo de procesos actuales
→ KPIs específicos antes del deploy
→ Roadmap de 90 días con milestones

ERROR #2: "El equipo se adapta solo"  
❌ Zero training al equipo
❌ Resistencia al cambio sin gestionar
❌ Expectativas irreales de adopción

✅ LO CORRECTO:
→ Change management desde día 1
→ Training hands-on de 2 semanas
→ Champions internos que evangelicen

ERROR #3: "Una vez y para siempre"
❌ Deploy and forget mentality
❌ No optimizar basado en datos
❌ No escalar conforme crece la empresa

✅ LO CORRECTO:
→ Monitoreo continuo de performance
→ A/B testing de diferentes approaches
→ Iteración mensual basado en feedback

🎯 RESULTADO: 89% de nuestros clientes ve ROI positivo en 45 días

¿Cometiste alguno de estos errores?
No pasa nada, son reversibles 💪

📞 ¿Auditamos tu implementación actual?
DM "AUDIT" para assessment gratuito.

#ErroresIA #ImplementaciónIA #TheAgents #TransformaciónDigital"""
        },
        {
            "image": "2026-03-08-theagents-post5-competencia.png",
            "date": "2026-03-19T13:00:00.000Z",
            "content": """🕵️ INTEL: Tu competencia ya se movió

DATOS QUE TE VAN A IMPACTAR:

📊 67% de empresas B2B ya implementaron algún tipo de automatización IA (McKinsey 2026)

🏃‍♂️ Early adopters reportan:
• 23% más velocidad en sales cycles
• 31% mejor conversión de leads  
• 45% reducción en customer acquisition cost
• 89% de su equipo "no volvería atrás"

🎯 INDUSTRIAS QUE MÁS ADOPTAN:
1. SaaS: 78% ya tiene agentes
2. E-commerce: 71% automatización avanzada  
3. Real Estate: 64% lead nurturing IA
4. Marketing Agencies: 61% client management IA
5. Consultoras: 58% proposal automation

⚡ LO QUE ESTÁ PASANDO AHORA:
→ Mientras leés esto, un agente IA está:
   • Respondiendo a TU prospect
   • Optimizando precios vs tu competencia
   • Automatizando procesos que vos haces manual
   • Escalando sin contratar más gente

🔥 PREGUNTA CRUCIAL:
¿Vas a liderar la transformación o vas a reaccionar cuando sea tarde?

💀 First-mover advantage se termina en 2026.

¿Tu estrategia IA está lista?

⚡ Comentá "READY" si querés estar en el 33% que lidera.

#CompetenciaIA #FirstMoverAdvantage #TheAgents #TransformaciónDigital #Liderazgo"""
        }
    ]
    
    # Initialize automation
    automation = PostizAutomation(API_KEY)
    
    # Get Instagram integration ID
    integrations = automation.get_integrations()
    instagram_integration = None
    
    if integrations:
        for integration in integrations:
            if integration.get('name') == 'Instagram' or 'instagram' in integration.get('provider', '').lower():
                instagram_integration = integration['id']
                break
    
    if not instagram_integration:
        print("Instagram integration not found. Make sure Instagram is connected in Postiz.")
        return
    
    print(f"Found Instagram integration: {instagram_integration}")
    
    # Upload images and create posts
    for i, post in enumerate(posts, 1):
        print(f"\n--- Processing Post {i}/5: {post['image']} ---")
        
        # Upload image
        image_obj = automation.upload_image(post['image'])
        if not image_obj:
            print(f"Skipping post {i} due to image upload failure")
            continue
        
        print(f"✅ Image uploaded: {image_obj['path']}")
        
        # Create scheduled post
        result = automation.create_scheduled_post(
            instagram_integration,
            post['content'], 
            image_obj,
            post['date']
        )
        
        if result:
            print(f"✅ Post {i} scheduled successfully for {post['date']}")
        else:
            print(f"❌ Failed to schedule post {i}")
    
    print("\n🎉 Automation complete! Check your Postiz dashboard.")

if __name__ == "__main__":
    main()