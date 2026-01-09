# Render Free Tier Deployment Guide

## Configuration Changes for Render Free Tier

This chatbot has been optimized for Render's free tier constraints:
- **512 MB RAM** (limited memory)
- **0.5 CPU** (limited computing power)
- **Auto-sleep** after 15 minutes of inactivity
- **Up to 750 hours/month** free tier quota

## Files Modified

### 1. **config.yml** (rasa_server/)
- ✅ Reduced DIET epochs: 100 → 50
- ✅ Reduced ResponseSelector epochs: 200 → 50
- ✅ Reduced TEDPolicy epochs: 200 → 100
- ✅ Reduced max_history: 5 → 3
- ✅ Added batch_size: 32 (reduces memory peaks)
- ✅ Reduced hidden_layers_sizes: [256, 128] → [128, 64]
- ✅ Removed LexicalSyntacticFeaturizer (memory intensive)
- ✅ Removed UnexpecTEDIntentPolicy (not critical for this use case)
- ✅ Max features limited to 2000 in CountVectorizer
- ✅ Learning rates optimized for faster convergence

### 2. **dockerfile** (rasa_server/)
- ✅ Added PYTHONUNBUFFERED=1 (real-time logging)
- ✅ Added RASA_LOG_LEVEL=WARNING (reduces memory from logging)
- ✅ Added environment variable configuration comments

### 3. **render.yaml** (root directory)
- ✅ Service type: web (Docker container)
- ✅ Memory: 512 MB
- ✅ CPU: 0.5 cores
- ✅ Plan: free
- ✅ Port: 5005
- ✅ Health check configured
- ✅ Telemetry disabled (saves resources)

## Deployment Steps

### Step 1: Prepare Your Repository
```bash
# Ensure all files are committed
git add .
git commit -m "Optimize for Render free tier deployment"
git push origin main
```

### Step 2: Create Render Account
1. Go to https://render.com
2. Sign up with GitHub account
3. Link your GitHub repository

### Step 3: Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select the branch (main/master)
4. Fill in service details:
   - **Name**: autism-chatbot-rasa
   - **Environment**: Docker
   - **Build Command**: (auto-detected from Dockerfile)
   - **Start Command**: (auto-detected from Dockerfile)

### Step 4: Configure Environment
In Render Dashboard:
1. Add Environment Variables:
   ```
   PYTHONUNBUFFERED=1
   RASA_LOG_LEVEL=WARNING
   RASA_TELEMETRY_ENABLED=false
   ```

2. Set Resource Limits (Free Tier):
   - Memory: 512 MB
   - CPU: 0.5

### Step 5: Deploy
1. Click "Create Web Service"
2. Render will automatically deploy
3. Initial deployment: ~3-5 minutes
4. Check logs in Render Dashboard

## Important Considerations for Free Tier

### ⚠️ Limitations You'll Experience
- **Auto-sleep**: Service stops after 15 min inactivity
- **Spin-up time**: ~30 seconds to wake from sleep
- **Cold starts**: First request takes longer
- **Concurrent connections**: Limited to reasonable number
- **750 hours/month**: Limited if running 24/7

### ✅ Best Practices
1. **Keep requests coming**: Set up monitoring/heartbeat to prevent sleep
   ```bash
   # Example: Keep-alive request every 10 minutes
   curl -X GET https://your-service.onrender.com/ -H "Accept: application/json"
   ```

2. **Monitor logs**: Check Render dashboard for crashes/errors
3. **Start simple**: Test with basic conversations first
4. **Scale if needed**: Upgrade to paid plan when needed

### 🔧 Performance Optimization
- Model loads once at startup (good for free tier)
- Keep conversations stateless
- Use response caching where possible
- Monitor memory usage in logs

## Testing After Deployment

### 1. Check Service is Running
```bash
curl https://your-service.onrender.com/status
```

### 2. Test NLU Intent Classification
```bash
curl -X POST https://your-service.onrender.com/model/parse \
  -H "Content-Type: application/json" \
  -d '{"text": "What is autism?"}'
```

### 3. Test Dialogue
```bash
curl -X POST https://your-service.onrender.com/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"message": "What is autism?"}'
```

## Troubleshooting

### Service Won't Start
- Check Render logs for errors
- Verify dockerfile path is correct
- Ensure model file exists: `models/latest.tar.gz`
- Check for YAML syntax errors in config.yml

### High Memory Usage
- Reduce epochs further if needed
- Consider smaller embedding dimensions
- Check for memory leaks in logs

### Timeout Errors
- Increase request timeout in client
- May be normal during auto-sleep wake-up
- Monitor Render dashboard for performance issues

### Model Not Loading
- Ensure models/latest.tar.gz exists and is valid
- Check file permissions
- Verify model was trained successfully: `rasa train`

## Next Steps

1. **Monitor**: Watch dashboard for errors/performance
2. **Test**: Send test messages through your interface
3. **Optimize**: Adjust config if needed based on performance
4. **Upgrade**: Move to paid plan if you exceed 750 hours/month

## Support & Resources
- Render Docs: https://render.com/docs
- Rasa Docs: https://rasa.com/docs/
- Check Render logs for detailed error messages

---

**Last Updated**: January 10, 2026
**Configuration**: Rasa 3.1 + Render Free Tier
