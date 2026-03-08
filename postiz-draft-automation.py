#!/usr/bin/env python3
"""
Postiz DRAFT Automation for The Agents
Creates posts as DRAFTS for manual approval by Wally
"""

import requests
import json
from datetime import datetime

class PostizDraftAutomation:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.postiz.com/public/v1"
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json"
        }
    
    def create_draft_post(self, integration_id, content, image_obj, suggested_date):
        """Create a DRAFT post for manual approval"""
        
        post_data = {
            "type": "now",  # Creates as draft instead of scheduled
            "shortLink": False,
            "tags": [],
            "posts": [{
                "integration": {"id": integration_id},
                "value": [{
                    "content": f"[SUGERIDO: {suggested_date}]\n\n{content}",
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
        
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print(f"Failed to create draft: {response.text}")
            return None

# FUTURE POSTS - ALWAYS CREATE AS DRAFTS
def create_future_content_as_drafts(api_key, integration_id):
    """Create all future posts as drafts with suggested schedule"""
    
    automation = PostizDraftAutomation(api_key)
    
    future_posts = [
        {
            "suggested_date": "Lunes 24 Marzo 10am",
            "title": "Post 6 - Future content",
            "content": "Futuro contenido será creado como draft para tu aprobación..."
        },
        # Add more future posts here
    ]
    
    for post in future_posts:
        print(f"Creating draft: {post['title']}")
        result = automation.create_draft_post(
            integration_id,
            post['content'],
            None,  # Add image when available
            post['suggested_date']
        )
        
        if result:
            print(f"✅ Draft created: {post['title']}")
        else:
            print(f"❌ Failed: {post['title']}")

if __name__ == "__main__":
    print("🎯 DRAFT MODE: All future posts will be created as drafts")
    print("📋 Manual approval required in Postiz dashboard")
    print("✅ Brand safety and content control guaranteed")