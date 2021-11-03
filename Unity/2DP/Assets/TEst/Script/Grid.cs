using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Grid : MonoBehaviour
{
    public Transform[] tiles;
    private void Start()
    {
        tiles = GetComponentsInChildren<Transform>();
        Debug.Log(tiles.Length);
        //TileArrange();
        
    }

    private void TileArrange()
    {
        float x = -4.5f;
        float z = -4.5f;
        for (int i = 0; i < 1; i++)
        {
            x = -4.5f;
            for (int j = 0; j < 10; j++)
            {
                tiles[10 * i + j].position
                    = new Vector3(x, 0.1f, z);
                x += 0.5f;
            }
            z += 1f;
        }
    }
}
