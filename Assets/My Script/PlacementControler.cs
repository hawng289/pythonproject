using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;

[RequireComponent(typeof(ARRaycastManager))]
public class PlacementControler : MonoBehaviour
{
    [SerializeField]
    private GameObject gameObjectToCreate;

    public GameObject placePrefab
    {
        get
        {
            return gameObjectToCreate;
        }
        set
        {
            gameObjectToCreate = value;
        }
    }

    ARRaycastManager arRaycastManager;
    private List<ARRaycastHit> hits = new List<ARRaycastHit>();

    public void Awake()
    {
        arRaycastManager = GetComponent<ARRaycastManager>();
    }

    private bool TryGetTouchPosition(out Vector2 touchPosition)
    {
        if (Input.touchCount > 0)
        {
            touchPosition = Input.GetTouch(0).position;
            return true;
        } 
        touchPosition = Vector2.zero;
        return false;
    }

    void Update()
    {
        if (!TryGetTouchPosition(out Vector2 touchPosition)) {
            return;
        }

        if (arRaycastManager.Raycast(touchPosition, hits, UnityEngine.XR.ARSubsystems.TrackableType.PlaneWithinPolygon))
        {
            var hitPose = hits[0].pose;
            Instantiate(placePrefab, hitPose.position, hitPose.rotation);
        }
    }
}
