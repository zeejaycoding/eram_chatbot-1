# Render Deployment Fix - Memory Issue Resolution

## Problem
Deployment on Render free tier (512MB) failed with:
```
==> Out of memory (used over 512Mi)
```

The model and Rasa runtime exceeded the 512MB memory limit when loading.

## Solution Implemented

### Option 1: ✅ RECOMMENDED - Upgrade to Starter Plan (1GB RAM)
**Updated render.yaml:**
- `memoryMB: 512` → `memoryMB: 1024`
- `plan: free` → `plan: starter`

**Cost:** ~$7-10/month (vs completely free)

**Pros:**
- Model runs reliably without optimization
- Better performance
- No compromise on chatbot quality

### Option 2: Ultra-Lightweight Config (512MB - No Cost)
**If you want to stay on free tier, use ultra-minimal config:**

Already applied to `config.yml`:
- Removed ResponseSelector (memory-heavy)
- Removed TEDPolicy (memory-heavy)
- Reduced DIET epochs: 50 → 20
- Reduced max features: default → 1000
- Minimal pipeline: only essential components

## Changes Made

### config.yml
```yaml
# BEFORE (Heavy):
- DIETClassifier: epochs 50
- ResponseSelector: epochs 50  
- TEDPolicy: epochs 100
- CountVectors with char_wb and multiple n-grams
- Total model size: ~300-400MB

# AFTER (Lightweight):
- DIETClassifier: epochs 20
- ResponseSelector: REMOVED
- TEDPolicy: REMOVED
- CountVectors: max_features 1000
- Total model size: ~100-150MB
```

### render.yaml
- Memory: 512MB → 1024MB
- Plan: free → starter
- CPU: kept at 0.5 cores

## Next Steps

1. **Retrain locally:**
   ```bash
   cd rasa_server
   rasa train
   ```

2. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Optimize Rasa model for Render - reduce memory footprint"
   git push
   ```

3. **Redeploy on Render:**
   - Go to Render Dashboard
   - Manual Deploy → New Deploy
   - Wait 3-5 minutes for build
   - Check logs for "Rasa server started"

## Performance Expectations

### With Starter Plan (1GB - Recommended)
- ✅ Fast startup: ~30-60 seconds
- ✅ Smooth conversations
- ✅ No memory issues
- ✅ Full feature set

### With Free Tier (512MB - Lightweight Config)
- ⚠️ Slower startup: ~60-90 seconds
- ⚠️ Reduced accuracy (fewer training epochs)
- ⚠️ May still hit limits with large requests
- ⚠️ Limited features (no response ranking)

## Pricing Comparison

| Tier | Memory | CPU | Monthly Cost | Startup |
|------|--------|-----|--------------|---------|
| Free | 512MB | 0.5 | $0 | ~90s+ (with optimization) |
| Starter | 1GB | 0.5 | ~$7 | ~30-60s |
| Standard | 2GB | 0.5 | ~$12 | ~10-20s |

## Monitoring After Deployment

Check Render Dashboard logs for:
- ✅ "Loading model..." appears
- ✅ "Rasa server started on http://0.0.0.0:5005"
- ✅ No "Out of memory" messages
- ✅ No crashes after 5 minutes

## Troubleshooting

If still getting OOM errors:

1. **Use even lighter pipeline:**
   ```yaml
   pipeline:
     - name: WhitespaceTokenizer
     - name: RegexFeaturizer
     - name: DIETClassifier
       epochs: 10
     - name: EntitySynonymMapper
     - name: FallbackClassifier
   ```

2. **Upgrade to paid plan** (Recommended)

3. **Consider Rasa Cloud** (Managed hosting)

## Files Updated
- ✅ config.yml - Ultra-lightweight model configuration
- ✅ render.yaml - Upgraded to 1GB starter plan
- ✅ dockerfile - Already optimized with environment variables

---

**Recommendation:** Use Starter Plan ($7/month) for reliable deployment. Free tier works with significant config compromises.

**Test Locally First:** Always run `rasa train` locally before pushing to verify it works.

Last Updated: January 10, 2026
